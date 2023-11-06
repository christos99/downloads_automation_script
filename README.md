# Downloads Folder Automation

This project includes a Python script that automates the process of organizing files in the Downloads folder into respective directories based on their file type. It also includes instructions to set up this script as a background service on macOS using `launchd`.

## Project Setup

### Step 1: Python Script

1. Create a Python script (`Downloads_automation.py`) that sorts files from the Downloads folder into specified directories.
2. The script uses the `os` and `shutil` modules to move files based on their extensions to predefined locations.
3. Make sure the script has the appropriate shebang line (`#!/usr/bin/env python3`) at the top to indicate which interpreter to use.
4. Grant execute permissions to the script using the terminal command `chmod +x Downloads_automation.py`.

### Step 2: Launchd Plist File

1. Create a Launch Agent plist file (`com.christos.downloadsautomation.plist`) in the `~/Library/LaunchAgents/` directory.
2. Define the necessary keys in the plist file, such as `Label`, `ProgramArguments`, `RunAtLoad`, `KeepAlive`, `StandardOutPath`, and `StandardErrorPath`.
3. Make sure `ProgramArguments` includes the path to the Python interpreter and the path to the Python script.
4. Load the plist file using `launchctl` to start the automation process.

### Step 3: Load the Launchd Job

1. Open Terminal and navigate to the Launch Agents directory: `cd ~/Library/LaunchAgents/`.
2. Load the plist file with `launchctl load com.christos.downloadsautomation.plist`.
3. Check if the launchd job is correctly loaded with `launchctl list | grep com.christos.downloadsautomation`.

### Step 4: Verify the Script Execution

1. Verify that the script is running correctly by checking the specified output and error log files.
2. Ensure that files are being sorted into the correct directories as intended.

## Troubleshooting

- If the script is not executing as expected, ensure that the paths in the plist file are correct.
- Use the `Console` app to review system logs for any errors or permission issues.
- Ensure that the script has the necessary permissions to execute and move files within the filesystem.

## Notes

- Be cautious with permissions. Only give the script the necessary access to perform its intended tasks.
- The provided setup instructions assume that the script and plist file are located within the user's home directory structure.
- If the downloads directory is not the default `~/Downloads`, adjust the script and plist paths accordingly.
