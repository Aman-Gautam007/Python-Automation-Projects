import pyautogui
import os
from datetime import datetime

def details():
    name = pyautogui.prompt("What is your name?")
    age = pyautogui.prompt("What is your age?")
    
    if name and age:
        save_details(name, age)

def save_details(name, age):
    """Save user details to a text file."""
    # Get the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    details_file = os.path.join(script_dir, "user_details.txt")
    
    # Prepare the details text
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    details_text = f"Name: {name}\nAge: {age}\nSaved on: {timestamp}\n{'-'*40}\n"
    
    # Append to the file
    with open(details_file, "a") as file:
        file.write(details_text)
    
    print(f"Details saved successfully to {details_file}")

if __name__ == "__main__":    details()

