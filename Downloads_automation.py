# /opt/homebrew/bin/python3


# This shebang line allows the script to be run as a standalone executable.

import os  # Used for file system path operations
import shutil  # Used for file operations like moving files

# Specify the directory where downloaded files are stored
downloads_path_1 = '/Users/christos/Downloads'
downloads_path_2 = '/Users/christos/Desktop'

# Define a dictionary that maps file extensions to their new destination folders
destinations = {
    'pdf': '/Users/christos/Downloads/Downloaded_Documents',
    'epub': '/Users/christos/Downloads/Downloaded_Books',
    'txt': '/Users/christos/Downloads/Downloaded_Documents',
    'jpg': '/Users/christos/Downloads/Downloaded_Images',
    'jpeg': '/Users/christos/Downloads/Downloaded_Images',
    'HEIC': '/Users/christos/Downloads/Downloaded_Images',
    'png': '/Users/christos/Downloads/Downloaded_Images',
    'mp3': '/Users/christos/Downloads/Downloaded_Music',  # Adding music files
    'mp4': '/Users/christos/Downloads/Downloaded_Videos',  # Adding video files
    'docx': '/Users/christos/Downloads/Downloaded_Documents',  # Adding Word documents
    'xlsx': '/Users/christos/Downloads/Downloaded_Documents',
    # Add more file types and destinations as needed
}


# Define the function that will sort and move the files
def sort_and_move_files(downloads_path, destinations):
    # Iterate over each file in the downloads directory
    for filename in os.listdir(downloads_path):
        # Construct the full file path
        file_path = os.path.join(downloads_path, filename)
        # Check if it is a file (and not a directory)
        if os.path.isfile(file_path):
            # Extract the file extension
            file_extension = filename.split('.')[-1].lower()
            # Look up the destination path for the given file extension
            dest_folder = destinations.get(file_extension)
            # If a destination is defined for the file type, move the file
            if dest_folder:
                # Construct the full destination path
                full_dest_path = os.path.join(dest_folder, filename)
                # Check if the file already exists at the destination to avoid overwrites
                if not os.path.exists(full_dest_path):
                    # Move the file to the destination folder
                    shutil.move(file_path, full_dest_path)
                    print(f"Moved: {filename} -> {dest_folder}")
                else:
                    # Notify user if the file already exists at the destination
                    print(f"File already exists at destination: {filename}")
            else:
                # Notify user if no destination is found for the file type
                print(f"No destination found for: {filename}. File is ignored.")


# Wrap the function call in a try-except block to handle potential exceptions
try:
    # Call the function to start sorting and moving files
    sort_and_move_files(downloads_path_1, destinations)
    sort_and_move_files(downloads_path_2, destinations)

except Exception as e:
    # Print any error that occurs during the file operation
    print(f"An error occurred: {e}")
