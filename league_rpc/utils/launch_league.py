import os
import platform
import subprocess
from argparse import Namespace
from typing import LiteralString

from league_rpc.logger.richlogger import RichLogger
from league_rpc.utils.const import (
    COMMON_DRIVES,
    DEFAULT_LEAGUE_CLIENT_EXE_PATH,
    DEFAULT_LEAGUE_CLIENT_EXECUTABLE,
)


def find_default_path() -> str | LiteralString:
    """Find the default path of the League Client executable."""
    # This function is originally for Windows logic.
    # We keep it because it sets the default value for argparse,
    # allowing us to detect if the user changed the path or not.

    # Check each drive for the executable
    for drive in COMMON_DRIVES:
        full_path = os.path.join(drive, DEFAULT_LEAGUE_CLIENT_EXE_PATH)
        if os.path.exists(full_path):
            return full_path
    # Fallback if the executable is not found
    return os.path.join("C:", DEFAULT_LEAGUE_CLIENT_EXE_PATH)


def launch_league_client(cli_args: Namespace, logger: RichLogger) -> None:
    """
    Launch the League Client with the given path or the default path.
    
    Args:
        cli_args: Command line arguments (contains launch_league path).
        logger: The existing logger instance (passed to avoid print conflicts).
    """
    
    # Platform check to ensure this only runs on macOS
    if platform.system() != "Darwin":
        logger.error(
            "This launch function is modified for macOS. Not on macOS.", color="red"
        )
        return

    # This is the default Windows path (e.g. C:\Riot Games...)
    default_win_path = find_default_path()
    
    # Standard League of Legends path on macOS
    default_mac_path = "/Applications/League of Legends.app"
    
    path_to_use = ""

    # Check if the user provided a custom path.
    # If the argument matches the Windows default OR the word "default" (from config.json)
    # then use the Mac standard path.
    if cli_args.launch_league == default_win_path or cli_args.launch_league == "default":
        # User did not provide a custom path, use the Mac default.
        path_to_use = default_mac_path
    else:
        # User provided a custom path (e.g., "/My/Path/League.app")
        path_to_use = cli_args.launch_league

    logger.info(f"Attempting to launch League at: {path_to_use}", color="green")

    try:
        # The 'open' command is the macOS equivalent of a double-click on the App
        subprocess.run(
            ["open", path_to_use],
            check=True,
        )
    # If it can't find the .app
    except FileNotFoundError:
        logger.error(
            f"Could not find League of Legends at: {path_to_use}", color="red"
        )
        logger.info("If your game is in a custom location, please update config.json.")
        logger.info('Example: "launch_league": "/Volumes/GameDrive/League of Legends.app"')
    # Other error
    except Exception as e:
        logger.error(f"Failed to launch League of Legends: {e}", color="red")