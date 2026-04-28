import subprocess
import time
import datetime
import pyautogui

def get_reminders_from_app():
    """Fetch reminders from macOS Reminders app"""
    script = """
    tell application "Reminders"
        return name of reminders whose completed is false
    end tell
    """
    result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
    return result.stdout.strip().split('\n')

time.sleep(2)

while True:
    reminders = get_reminders_from_app()
    for reminder in reminders:
        if reminder:
            print(f"{datetime.datetime.now()} - {reminder}")
            pyautogui.typewrite(reminder)
            pyautogui.press("enter")
            time.sleep(5)
    
    time.sleep(60)  # Check reminders every minute