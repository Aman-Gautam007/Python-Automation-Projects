import subprocess
import time
import datetime
import pyautogui

def get_events_from_calendar():
    """Fetch events from macOS Calendar app"""
    script = """
    tell application "Calendar"
        set eventList to ""
        repeat with cal in calendars
            repeat with evt in (events of cal whose start date is greater than (current date))
                set eventList to eventList & name of evt & " at " & start date of evt & linefeed
            end repeat
        end repeat
        return eventList
    end tell
    """
    result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
    return result.stdout.strip().split('\n')

time.sleep(2)

while True:
    events = get_events_from_calendar()
    for event in events:
        if event:
            print(f"{datetime.datetime.now()} - {event}")
            pyautogui.typewrite(event)
            pyautogui.press("enter")
            time.sleep(5)
    
    time.sleep(10)  # Check calendar 10 seconds after posting events