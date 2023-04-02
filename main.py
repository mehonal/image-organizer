import os
import shutil
import datetime
from pathlib import Path

print("Starting script.")

class SETTINGS:
    EXTENSIONS = [".jpeg",".jpg",".png",".svg"]
    USE_MODIFIED_TIME = True
    REVERT_CHANGES_MODE = False
    YEAR_FOLDER = True # makes a folder for each year
    MONTH_FOLDER = True # makes a folder for each month
    DAY_FOLDER = True  # makes a folder for each day
    HOUR_FOLDER = False  # makes a folder for each hour
    MINUTE_FOLDER = False  # makes a folder for each minute

if SETTINGS.REVERT_CHANGES_MODE:
    root_directory = Path('.')
    size = 0
    for file in root_directory.glob("**/*"):
        if file.name.endswith(tuple(SETTINGS.EXTENSIONS)):
            print(f"Moving {file} to root directory.")
            shutil.move(file, os.getcwd() + "/" + file.name)
else:
    for file in os.listdir():
        if file.endswith(tuple(SETTINGS.EXTENSIONS)):
            if SETTINGS.USE_MODIFIED_TIME:
                file_timestamp = os.path.getmtime(file)
            else:
                file_timestamp = os.path.getctime(file)        
            file_date = datetime.datetime.fromtimestamp(file_timestamp)
            print(f'Date: {file_date}')
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
            path_exists = False
            Path(folder_path).mkdir(parents=True, exist_ok=True)
            if os.path.exists(folder_path):
                print(f"Moving {file} to {folder_path}")
                shutil.move(os.getcwd() + "/" + file, folder_path + "/" + file)
            else:
                print(f"Missing folder!")

print("Script finished executing.")