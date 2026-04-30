import pyautogui
import os
import shutil
from pathlib import Path

# Define the file to manage
file_path = Path(__file__).parent / "user_details.txt"

# Create backup folder if it doesn't exist
backup_folder = Path(__file__).parent / "Backup"
backup_folder.mkdir(exist_ok=True)

response = pyautogui.confirm("What do want to do with the file?", buttons=["Move", "Delete", "Skip"])
if response == "Move":
    if file_path.exists():
        backup_file_path = backup_folder / file_path.name
        shutil.move(str(file_path), str(backup_file_path))
        pyautogui.alert(f"The file has been moved to: {backup_folder}")
    else:
        pyautogui.alert("File not found!")
elif response == "Delete":
    confirm = pyautogui.confirm("Are you sure you want to delete the file?", buttons=["Yes", "No"])
    if confirm == "Yes":
        if file_path.exists():
            file_path.unlink()
            pyautogui.alert("The file has been deleted successfully.")
        else:
            pyautogui.alert("File not found!")
    else:
        pyautogui.alert("The file will not be deleted and will remain in its current location.")
else:
    pyautogui.alert("The file will be skipped and left in its current location.")