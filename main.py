import os
import shutil
import datetime
from pathlib import Path

print("Starting script.")

class SETTINGS:
    EXTENSIONS = [".jpeg",".jpg",".png",".svg"] # note: this is case sensitive
    USE_MODIFIED_TIME = True
    REVERT_CHANGES_MODE = False
    YEAR_FOLDER = True # makes a folder for each year
    MONTH_FOLDER = True # makes a folder for each month
    DAY_FOLDER = True  # makes a folder for each day
    HOUR_FOLDER = False  # makes a folder for each hour
    MINUTE_FOLDER = False  # makes a folder for each minute
    LOG_OPERATIONS = True # logs operations performed in a log file
    LOG_FILE_NAME =  'image_operations.log' # only used if LOG_OPERATIONS is set to True; name of the log file
    OVERWRITE_LOG_FILE = True # if set to True, it overwrites previous logs of operations from the past (assuming the log file name has not changed)


if SETTINGS.LOG_OPERATIONS:
    if SETTINGS.OVERWRITE_LOG_FILE:
        mode = 'w'
    else:
        mode = 'a'
    log_file = open(SETTINGS.LOG_FILE_NAME, mode)
    log_file.write(f"-----------------------------------------------\n")
    start = datetime.now()
    log_file.write(f"Log Initiated: {start}\n")
    del mode

if SETTINGS.REVERT_CHANGES_MODE:
    root_directory = Path('.')
    size = 0
    for file in root_directory.glob("**/*"):
        if file.name.endswith(tuple(SETTINGS.EXTENSIONS)):
            log = f"Moving {file} to root directory."
            print(log)
            if SETTINGS.LOG_OPERATIONS:
                log_file.write(log + "\n")
            shutil.move(file, os.getcwd() + "/" + file.name)
else:
    for file in os.listdir():
        if file.endswith(tuple(SETTINGS.EXTENSIONS)):
            if SETTINGS.USE_MODIFIED_TIME:
                file_timestamp = os.path.getmtime(file)
            else:
                file_timestamp = os.path.getctime(file)        
            file_date = datetime.datetime.fromtimestamp(file_timestamp)
            if file_date and file_date is not None:
                log = f'{file}: {file_date}'
                print(log)
                if SETTINGS.LOG_OPERATIONS:
                    log_file.write(log + "\n")
                folder_path = ""
                if SETTINGS.YEAR_FOLDER:
                    folder_path += str(file_date.year) + "/"
                if SETTINGS.MONTH_FOLDER:
                    folder_path += str(file_date.month) + "/"
                if SETTINGS.DAY_FOLDER:
                    folder_path += str(file_date.day) + "/"
                if SETTINGS.HOUR_FOLDER:
                    folder_path += str(file_date.hour) + "/"
                if SETTINGS.MINUTE_FOLDER:
                    folder_path += str(file_date.minute) + "/"
                if folder_path[-1] == "/":
                    folder_path = folder_path[:-1]
                print(folder_path)
                Path(folder_path).mkdir(parents=True, exist_ok=True)
                if folder_path != "":
                    if os.path.exists(folder_path):
                        log = f"Moving {file} to {folder_path}"
                        print(log)
                        if SETTINGS.LOG_OPERATIONS:
                            log_file.write(log + "\n")
                        shutil.move(os.getcwd() + "/" + file, folder_path + "/" + file)
                    else:
                        log = f"Missing folder \"{folder_path}\"!"
                        print(log)
                        if SETTINGS.LOG_OPERATIONS:
                            log_file.write(log + "\n")
                else:
                    log = f"Skipped file: {file}"
                    print(log)
                    if SETTINGS.LOG_OPERATIONS:
                        log_file.write(log + "\n")

if SETTINGS.LOG_OPERATIONS:
    end = datetime.now()
    log_file.write(f"Log Finished: {end}\n")
    time_elapsed = (end - start).total_seconds()
    log_file.write(f"Total Time Elapsed: {time_elapsed}\n")
    log_file.close()

print("Script finished executing.")