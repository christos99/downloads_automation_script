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

### Step 5: Reloading the Launchd Job

If you make changes to the `Downloads_automation.py` script or the `com.christos.downloadsautomation.plist` file after the initial load, you will need to reload the plist for changes to take effect. Here's how to properly reload the launchd job:

1. Before reloading the plist file, it must first be unloaded.
   - In Terminal, execute: `launchctl unload ~/Library/LaunchAgents/com.christos.downloadsautomation.plist`
   - Or alternatively `launchctl bootout ~/Library/LaunchAgents/com.christos.downloadsautomation.plist`
   - This command will remove the job from `launchd` management.
4. After unloading, you can reload the plist file with:
   - `launchctl load ~/Library/LaunchAgents/com.christos.downloadsautomation.plist`
   - Or alternatively `launchctl boostrap ~/Library/LaunchAgents/com.christos.downloadsautomation.plist`
   - This will load the updated job into `launchd`.
5. If you encounter an "Input/output error" upon reloading, confirm that:
   - You are in the correct directory in the Terminal. If not, navigate to the correct directory using `cd`.
   - The plist file path is correct and the file permissions allow reading by `launchd`.
   - There are no syntax errors in the plist file. You can check this with `plutil -lint ~/Library/LaunchAgents/com.christos.downloadsautomation.plist`.
6. It's also a good practice to check the Console app for any specific error messages related to `launchd` and your plist file.
7. Always verify that the service is loaded and running with the correct configuration by using:
   - `launchctl list | grep com.christos.downloadsautomation`
   - This command should output information about the job if it is running, or no output if it is not loaded.
8. Remember that any changes to the environment or context in which the script runs may require adjustments to the plist file and a subsequent reload.

By following these steps, you can ensure that your `launchd` job is up to date and functioning as intended.

## Notes

- Always back up your plist file before making changes, so you can restore the previous version if something goes wrong.
- Keep in mind that `launchctl load` or `unload` will only work on user agents when executed as the logged-in user and not
- As `root` or with `sudo` try running the `bootstrap` or with `bootout`



## Troubleshooting

- If the script is not executing as expected, ensure that the paths in the plist file are correct.
- Use the `Console` app to review system logs for any errors or permission issues.
- Ensure that the script has the necessary permissions to execute and move files within the filesystem.

## Notes

- Be cautious with permissions. Only give the script the necessary access to perform its intended tasks.
- The provided setup instructions assume that the script and plist file are located within the user's home directory structure.
- If the downloads directory is not the default `~/Downloads`, adjust the script and plist paths accordingly.
