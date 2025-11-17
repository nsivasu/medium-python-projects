import datetime
import time
import winsound

alarm_time = input("Alarm time (HH:MM:SS): ")
message = input("Your alarm message: ")

while True:
    if datetime.datetime.now().strftime("%H:%M:%S") == alarm_time:
        print(" ALARM:", message)
        
        for _ in range(5):  # Repeat beep 5 times
            winsound.Beep(1500, 700)
            time.sleep(0.3)
        break
    time.sleep(1)
