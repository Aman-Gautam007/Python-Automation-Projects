import pyautogui
import time
import datetime

reminders = [
    "Reminder: Drink water!",
    "Reminder: Take medicine!",
    "Reminder: Take the dog for a walk!"
]

def send_reminder(reminder):
    print(datetime.datetime.now())
    pyautogui.confirm(reminder, buttons=["OK", "Remind Later"])

for reminder in reminders:
    send_reminder(reminder)
    time.sleep(30)