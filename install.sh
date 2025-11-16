#!/bin/bash

# ------------------------------------------------------------------
#  Automatic Installer for league-mac-rpc
#  This script installs Homebrew, Python 3.11, and all dependencies.
# ------------------------------------------------------------------

echo "👑 Starting installation for LeagueRPC..."

# --- Find the project directory ---
# Change to the directory where this script is located
# (this allows the user to run it from anywhere)
cd "$(dirname "$0")"
PROJECT_DIR=$(pwd)
echo "Installing in directory: $PROJECT_DIR"


# --- Install Homebrew or check if it's already installed ---
echo "Checking for Homebrew..."
if ! command -v brew &> /dev/null; then
    echo "Homebrew not found. Starting installation."
    echo "ATTENTION: You will need to enter your Mac password when prompted to install Homebrew."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    
    # Add Homebrew to the PATH for this session
    export PATH="/opt/homebrew/bin:$PATH"
    echo "Homebrew installed."
else
    echo "Homebrew is already installed."
fi


# --- Install Python 3.11 (if not present) ---
echo "Checking for Python 3.11..."
if ! brew list python@3.11 &> /dev/null; then
    echo "Installing Python 3.11... (this may take a few minutes)"
    brew install python@3.11
else
    echo "Python 3.11 is already installed."
fi

# Define the exact Python executable we will use
PYTHON_EXE="/opt/homebrew/opt/python@3.11/bin/python3.11"


# --- Create the virtual environment ---
echo "Configuring virtual environment (venv)..."
if [ ! -d "venv" ]; then
    $PYTHON_EXE -m venv venv
    echo "Environment created."
else
    echo "Environment 'venv' already exists."
fi


# --- Install all dependencies ---
echo "Installing required Python libraries..."
"$PROJECT_DIR/venv/bin/pip" install --upgrade pip setuptools
"$PROJECT_DIR/venv/bin/pip" install -r requirements.txt
"$PROJECT_DIR/venv/bin/pip" install -e .
echo "Libraries installed."


# --- Create the launcher ---
echo "Creating 'StartLoL_RPC.command' in the project directory..."
LAUNCHER_PATH="$PROJECT_DIR/StartLoL_RPC.command"
LAUNCHER_CONTENT="#!/bin/bash
# Script to start LeagueRPC
# Change directory to the project folder
cd \"$PROJECT_DIR\"
# Start the program using the venv's Python
./venv/bin/python3 -m league_rpc
"
# Write the file
echo "$LAUNCHER_CONTENT" > "$LAUNCHER_PATH"
# Make it executable
chmod +x "$LAUNCHER_PATH"


# --- Done! ---
echo ""
echo "---------------------------------------------------------"
echo "✅  INSTALLATION COMPLETE! ✅"
echo ""
echo "I created a file in the project folder called 'StartLoL_RPC.command'."
echo "From now on, just double-click that file to start the program!"
echo ""
echo "---------------------------------------------------------"