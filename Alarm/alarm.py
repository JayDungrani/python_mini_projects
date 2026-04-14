import datetime
import time
import winsound
from playsound import playsound
import re
from pathlib import Path


def getAlarm_time():
    print("Enter in this format : 12:05")
    alarm_time = input("Set Alarm : ")
    return alarm_time

def setAlarm(alarm_time):
    if re.search(r"^\d\d:\d\d$",alarm_time):
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M")
            if(alarm_time==current_time):
                # winsound.Beep(1000,2000)
                playsound(f"{Path.cwd()}/alarm_audio.wav")
                print("Wake Up")
                break
            time.sleep(1)
    else:
        raise ValueError("Invalid Time")


def main():
    alarm_time = getAlarm_time()
    setAlarm(alarm_time)

if __name__ == "__main__":
    main()
