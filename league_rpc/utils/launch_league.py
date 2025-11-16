import os
import platform  # Importato qui
import subprocess
from argparse import Namespace
from typing import LiteralString

from league_rpc.logger.richlogger import RichLogger  # Importato qui
from league_rpc.utils.const import (
    COMMON_DRIVES,
    DEFAULT_LEAGUE_CLIENT_EXE_PATH,
    DEFAULT_LEAGUE_CLIENT_EXECUTABLE,
)


def find_default_path() -> str | LiteralString:
    """Find the default path of the League Client executable."""
    # This function is for Windows, but we keep it
    # because its return value is used as the default
    # for the --launch-league argument.

    # Check each drive for the executable
    for drive in COMMON_DRIVES:
        full_path = os.path.join(drive, DEFAULT_LEAGUE_CLIENT_EXE_PATH)
        if os.path.exists(full_path):
            return full_path
    # Fallback if the executable is not found
    return os.path.join("C:", DEFAULT_LEAGUE_CLIENT_EXE_PATH)


def launch_league_client(cli_args: Namespace) -> None:
    """Launch the League Client with the given path or the default path."""
    
    logger = RichLogger()

    # Platform check to ensure this only runs on macOS
    if platform.system() != "Darwin":
        logger.error(
            "This launch function is modified for macOS. Not on macOS.", color="red"
        )
        return

    # This is the default Windows path, used as the default
    # value for the --launch-league argument.
    default_win_path = find_default_path()
    
    # Standard League of Legends path on macOS
    default_mac_path = "/Applications/League of Legends.app"
    
    path_to_use = ""

    # Check if the user provided a custom path.
    # If the argument still has the Windows default path, it means the user provided nothing.
    if cli_args.launch_league == default_win_path:
        # User did not provide a custom path, use the Mac default.
        path_to_use = default_mac_path
    else:
        # User provided a custom path
        path_to_use = cli_args.launch_league

    logger.info(f"Attempting to launch League at: {path_to_use}")

    try:
        # Opening League of Legends.app
        subprocess.run(
            ["open", path_to_use],
            check=True,
        )
    # If it can't find the .app
    except FileNotFoundError:
        logger.error(
            f"Could not find League of Legends at: {path_to_use}", color="red"
        )
        logger.info("If your game is in a custom location, make sure to specify the full path:")
        logger.info("--launch-league \"/Full/Path/To/League of Legends.app\"")
    # Other error
    except Exception as e:
        logger.error(f"Failed to launch League of Legends: {e}", color="red")