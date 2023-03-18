import os
import shutil
import datetime
from pathlib import Path

print("Starting script.")

class SETTINGS:
    EXTENSIONS = [".jpeg",".png"]
    USE_MODIFIED_TIME = True
    REVERT_CHANGES_MODE = True

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
            folder_path = f"{file_date.year}/{file_date.month}/{file_date.day}"
            print(folder_path)
            path_exists = False
            Path(folder_path).mkdir(parents=True, exist_ok=True)
            if os.path.exists(folder_path):
                print(f"Moving {file} to {folder_path}")
                shutil.move(os.getcwd() + "/" + file, folder_path + "/" + file)
            else:
                print(f"Missing folder!")

print("Script finished executing.")