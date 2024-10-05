import time
from datetime import datetime
from playsound import playsound

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")

    while True:
        current_time = datetime.now().strftime("%H:%M:%S")

        if current_time == alarm_time:
            print("Time to wake up!")
            playsound(r'D:\CODE\Python\Basic-projects\alarm_sound.mp3')  
            break
            
        time.sleep(1)


def main():
    alarm_time = input("Enter the alarm time in HH:MM:SS format: ")
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()