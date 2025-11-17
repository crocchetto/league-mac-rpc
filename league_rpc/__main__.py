import nest_asyncio
nest_asyncio.apply()

import argparse
import sys
import threading
import time
import json
import os
import subprocess
import shlex
import logging

# nest_asyncio is imported twice in the original logic to ensure stability; keeping it.
import nest_asyncio  # type:ignore

from league_rpc.lcu_api.lcu_connector import start_connector
from league_rpc.logger.richlogger import RichLogger
from league_rpc.processes.process import (
    check_discord_process,
    check_league_client_process,
)
from league_rpc.utils.color import Color
from league_rpc.utils.const import DEFAULT_CLIENT_ID, DISCORD_PROCESS_NAMES
from league_rpc.utils.launch_league import find_default_path


# --- CRASH FIX FILTER ---
class CrashFixFilter(logging.Filter):
    """
    A smart filter that intercepts log messages before they are written.
    If a message is malformed (causing a TypeError during formatting),
    this filter blocks it, preventing the application from crashing.
    Specific fix for the 'lcu_driver' library bug.
    """
    def filter(self, record):
        try:
            # Attempt to format the message ahead of time.
            # If this fails, the message is bugged.
            if record.args:
                str(record.msg) % record.args
            return True  # Message is safe, let it pass
        except TypeError:
            # Found the killer message! Block it.
            return False


# --- MACOS TERMINAL HELPER ---
def ensure_terminal_output():
    """
    macOS SPECIFIC:
    When a .app is launched via double-click, it runs without a visible console.
    This function detects if the app is running 'silently' and restarts the application
    inside a new visible Terminal window so the user can view the logs.
    """
    # Check if we are running as a frozen executable (App) on macOS
    if getattr(sys, 'frozen', False) and sys.platform == 'darwin':
        # Check if we have a terminal attached. If not, we are in "double-click" mode.
        if not sys.stdout.isatty():
            # Check for the internal flag to prevent infinite loops
            if "--internal-terminal" not in sys.argv:
                executable = sys.executable
                safe_exec = shlex.quote(executable)
                
                # Command: run the app adding the secret flag
                cmd = f"{safe_exec} --internal-terminal"
                
                # AppleScript command to tell Terminal.app to run this executable
                script = f'tell application "Terminal" to do script "{cmd}" activate'
                
                subprocess.run(["osascript", "-e", script])
                
                # Terminate this silent instance immediately.
                # The new instance in the Terminal will take over.
                sys.exit(0)


# --- CONFIGURATION LOADER ---
def load_config_file(args_namespace):
    """
    Loads configuration from a 'config.json' file to override CLI arguments.
    
    - If running as a standalone Python script, it looks in the project root.
    - If running as a compiled macOS App (.app), it looks inside Contents/Resources.
    """
    
    # 1. Determine the base path where config.json should be located
    if getattr(sys, 'frozen', False):
        if sys.platform == 'darwin':
            # CASE: macOS App Bundle (.app)
            # Structure: LeagueRPC.app/Contents/MacOS/LeagueRPC (executable)
            # Target:    LeagueRPC.app/Contents/Resources/config.json
            executable_path = os.path.dirname(sys.executable)
            contents_path = os.path.dirname(executable_path)
            resources_path = os.path.join(contents_path, "Resources") 
            config_path = os.path.join(resources_path, "config.json")
        else:
            # CASE: Windows/Linux frozen executable
            config_path = os.path.join(os.path.dirname(sys.executable), "config.json")
    else:
        # CASE: Standard Python Script
        # Target: Project root directory (one level up from this file)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = os.path.dirname(current_dir)
        config_path = os.path.join(base_dir, "config.json")

    # Debug print (visible in the terminal)
    print(f"[DEBUG] Looking for config at: {config_path}")
    
    # 2. If config doesn't exist, return existing args unchanged
    if not os.path.exists(config_path):
        print("[INFO] Config file not found, using default arguments.")
        return args_namespace

    # 3. Load and apply settings
    try:
        with open(config_path, 'r') as f:
            config_data = json.load(f)
        
        print("[INFO] Config file found! Applying settings...")
        
        for key, value in config_data.items():
            # Convert JSON keys (e.g., "launch-league") to Python args (e.g., "launch_league")
            key_fixed = key.replace("-", "_")
            
            # Update the argument if it exists in the namespace
            if hasattr(args_namespace, key_fixed):
                setattr(args_namespace, key_fixed, value)
                # print(f"  -> Set '{key_fixed}' to: {value}") # Uncomment for verbose debug
                
    except Exception as e:
        print(f"[ERROR] Failed to load config.json: {e}")

    return args_namespace


def main(cli_args: argparse.Namespace) -> None:
    """
    This is the program that gets executed.
    """
    
    # Apply the CrashFixFilter to the lcu_driver logger
    logging.getLogger("lcu_driver").addFilter(CrashFixFilter())

    logger = RichLogger(show_debugs=cli_args.debug)
    logger.start_progress_bar(name="Checking League")
    ############################################################
    ## Check Discord, RiotClient & LeagueClient processes     ##
    check_league_client_process(cli_args, logger)

    logger.stop_progress_bar()

    logger.start_progress_bar(name="Checking Discord")
    rpc = check_discord_process(
        process_names=DISCORD_PROCESS_NAMES + cli_args.add_process,
        client_id=cli_args.client_id,
        wait_for_discord=cli_args.wait_for_discord,
        logger=logger,
    )
    logger.stop_progress_bar()

    # Start LCU_Thread
    # This process will connect to the LCU API and updates the rpc based on data subscribed from the LCU API.
    # In this case passing the rpc object to the process is easier than trying to return updated data from the process.
    # Every In-Client update will be handled by the LCU_Thread process and will update the rpc accordingly.
    lcu_process = threading.Thread(
        target=start_connector,
        args=(
            rpc,
            cli_args,
            logger,
        ),
        daemon=True,
    )
    lcu_process.start()

    try:
        while lcu_process.is_alive():
            time.sleep(1)
    except KeyboardInterrupt as e:
        logger.info(f"{e.__class__.__name__} detected. Shutting down the program..")
        rpc.close()
        sys.exit(0)

    ############################################################


if __name__ == "__main__":
    # Ensure we have a visible terminal on macOS
    ensure_terminal_output()
    
    # Patch for asyncio
    nest_asyncio.apply()  # type: ignore

    default_league_path = find_default_path()

    parser = argparse.ArgumentParser(description="Script with Discord RPC.")
    parser.add_argument(
        "--client-id",
        type=str,
        default=DEFAULT_CLIENT_ID,
        help=f"Client ID for Discord RPC. Default is {DEFAULT_CLIENT_ID}. which will show 'League of Legends' on Discord",
    )
    parser.add_argument(
        "--no-stats",
        action="store_true",
        help="use '--no-stats' to Opt out of showing in-game stats (KDA, minions) in Discord RPC",
    )
    parser.add_argument(
        "--hide-emojis",
        action="store_true",
        help="use '--hide-emojis' to hide the green/red circle emoji, depending on your Online status in league.",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="use '--debug' to see additional logging data. Otherwise logs from INFO -> CRITICAL will show. Debug logs are hidden by default",
    )
    parser.add_argument(
        "--no-rank",
        action="store_true",
        help="use '--no-rank' to hide your SoloQ/Flex/Tft/Arena Rank in Discord RPC",
    )
    parser.add_argument(
        "--add-process",
        nargs="+",
        default=[],
        help="Add custom Discord process names to the search list.",
    )
    parser.add_argument(
        "--wait-for-league",
        type=int,
        default=-1,
        help="Time in seconds to wait for the League client to start. -1 for infinite waiting, Good when used as a starting script for league.",
    )
    parser.add_argument(
        "--wait-for-discord",
        type=int,
        default=-1,
        help="Time in seconds to wait for the Discord client to start. -1 for infinite waiting, Good when you want to start this script before you've had time to start Discord.",
    )
    parser.add_argument(
        "--launch-league",
        type=str,
        default=default_league_path,
        help=f"Path to the League of Legends client executable. Default path is: {default_league_path}",
    )
    parser.add_argument(
        "--hide-in-client",
        action="store_true",
        help="Temporarily hides the League of Legends Rich Presence while you're idle in the client only. The presence will automatically reactivate when you enter a lobby, queue, champ select, or game.",
    )
    
    # SECRET ARGUMENT (Prevents argparse crash during restart)
    parser.add_argument("--internal-terminal", action="store_true", help=argparse.SUPPRESS)

    args: argparse.Namespace = parser.parse_args()

    # CONFIGURATION LOADING
    # Overwrite CLI args with config.json values if present.
    args = load_config_file(args)
    
    # If config has "default" string, revert to constant ID
    if args.client_id == "default":
        args.client_id = DEFAULT_CLIENT_ID

    # Prints the League RPC logo
    print(Color().logo)

    # Discord server information for support and other projects
    print(f"{Color.blue}{'─' * 60}{Color.reset}")
    print(f"{Color.green}• Need help? Contact me @crocchetto on Discord or join here: {Color.cyan}https://discord.haze.sh{Color.reset}")
    print(f"{Color.green}• Like LeagueRPC? You'll love {Color.orange}DJ Braum{Color.green} - Music bot for you & your friends: {Color.cyan}https://braum.haze.sh{Color.reset}")
    print(f"{Color.green}• Portfolio & more projects: {Color.cyan}https://haze.sh{Color.reset} {Color.green}Be careful of the 🦆. It might get angry!{Color.reset}")
    print(f"{Color.blue}{'─' * 60}{Color.reset}\n")

    if args.hide_in_client:
        print(
            f"{Color.green}Argument {Color.blue}--hide-in-client{Color.green} detected.. Will hide the in-client Rich presence.{Color.reset}"
        )
    if args.no_stats:
        print(
            f"{Color.green}Argument {Color.blue}--no-stats{Color.green} detected.. Will {Color.red}not {Color.green}show InGame stats{Color.reset}"
        )
    if args.no_rank:
        print(
            f"{Color.green}Argument {Color.blue}--no-rank{Color.green} detected.. Will hide your league rank.{Color.reset}"
        )
    if args.hide_emojis:
        print(
            f"{Color.green}Argument {Color.blue}--hide-emojis{Color.green} detected.. Will hide emojis. such as league status indicators on Discord.{Color.reset}"
        )
    if args.debug:
        print(
            f"{Color.green}Argument {Color.blue}--debug{Color.green} detected.. Will show debug logs.{Color.reset}"
        )
    if args.add_process:
        print(
            f"{Color.green}Argument {Color.blue}--add-process{Color.green} detected.. Will add {Color.blue}{args.add_process}{Color.green} to the list of Discord processes to look for.{Color.reset}"
        )

    if args.client_id != DEFAULT_CLIENT_ID:
        print(
            f"{Color.green}Argument {Color.blue}--client-id{Color.green} detected.. Will try to connect by using {Color.blue}({args.client_id}){Color.reset}"
        )
    if args.wait_for_league and args.wait_for_league > 0:
        print(
            f"{Color.green}Argument {Color.blue}--wait-for-league{Color.green} detected.. {Color.blue}will wait for League to start before continuing{Color.reset}"
        )
    if args.wait_for_discord and args.wait_for_discord > 0:
        print(
            f"{Color.green}Argument {Color.blue}--wait-for-discord{Color.green} detected.. {Color.blue}will wait for Discord to start before continuing{Color.reset}"
        )

    if args.launch_league:
        if args.launch_league == default_league_path or args.launch_league == "default":
            print(
                f"{Color.green}Attempting to launch the League client at the default location{Color.reset} {Color.blue}{default_league_path}{Color.reset}\n"
                f"{Color.green}If league is already running, it will not launch a new instance.{Color.reset}\n"
                f"{Color.orange}If the League client does not launch, please specify the path manually using config.json or: --launch-league <path>{Color.reset}\n"
            )
        else:
            print(
                f"{Color.green}Detected custom path. Launching from: {Color.blue}{args.launch_league}{Color.reset}\n"
                f"{Color.orange}If league is already running, it will not launch a new instance.{Color.reset}\n"
            )

    main(cli_args=args)
    