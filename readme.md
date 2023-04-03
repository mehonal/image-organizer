Status: Work in progress

This is a Python Script that organize images, or other files based on the date they were made, or last modified.

# How to use the script
The script needs to be located at the root directory of the images to scan them and organize them into folders based on their dates.

# Settings

Currently, settings are embedded into the script file itself under the class `SETTINGS`. You may tweak these settings to your liking. The current settings are:

- EXTENSIONS: An array of the file extensions that determines which files in the relevant directories should be used by the script
- USE_MODIFIED_TIME: If set to `True`, it will use the time a file or image was last modified to perform the moving operations. If set to `False`, the script will use the "Created Time" tied to the file. You may play around with this setting to see which of these options suits your case better.
- REVERT_CHANGES_MODE: If set to `True`, it will run the script in reverse mode, moving all files that end with the desired extensions back to the root directory from their location.
- YEAR_FOLDER: If set to `True`, it will include the year in the folder hierarchy.
- MONTH_FOLDER: If set to `True`, it will include the month in the folder hierarchy.
- DAY_FOLDER: If set to `True`, it will include the day in the folder hierarchy.
- HOUR_FOLDER: If set to `True`, it will include the hour in the folder hierarchy.
- MINUTE_FOLDER: If set to `True`, it will include the minute in the folder hierarchy.
- LOG_OPERATIONS: If set to `True`, it will log operations in a log file stored in the root directory of the script.
- LOG_FILE_NAME: The name of the log file keeping the logs of the operations.
- OVERWRITE_LOG_FILE: If set to `True`, any previous log files with the current LOG_FILE_NAME will be overwritten. If set to `False`, previous operations that were logged will be preserved, and the new operations will be appended.



# Compatibility
The script has been tested to work on Linux and Windows for core functionality. Further testing is needed on both operating systems.

# Warnings
- The script is still Work-In-Progress, and lacks enough testing so please be cautious with using it.
- The REVERT_CHANGES_MODE currently recursively checks all folders in the root directory, and will move files with the matching file extensions regardless of whether they were moved by the script in the first place.
- Please be cautious with using the script on a directory with subdirectories. This could result in undesired results (for instance, if REVERT_CHANGES_MODE is set to `True`, all relevant files will be recursively moved to the root from subdirectories that may not have been made from the script).

# Planned Features & Changes
- Optional setting to automatically delete folders after script is executed with REVERT_CHANGES_MODE
- Optional setting to enable analyzing file names to extract date from them