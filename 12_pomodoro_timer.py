import time
import sys
from playsound import playsound

def countdown(seconds,message):
    while seconds > 0:
        mins ,secs = divmod(seconds ,60 )
        time_format = f'{mins:02}:{secs:02}'
        print(time_format , end='\r')
        time.sleep(1)
        seconds -= 1

def main():
    work_time=int(input("Enetr the time you want to work for in minutes:"))
    break_time=int(input("Enter break time in minutes:"))
    # converting to seconds for better calculation
    work_seconds = work_time * 60
    break_seconds = break_time * 60

    cycles = int(input("Enter the number of pomodoro cycles:"))
    # checking if pomodoro is 0
    if cycles == 0:
        print("why u even using this program")
        sys.exit()

    for cycle in range(cycles):
        print(f"Pomodoro Cycle {cycle + 1}")

        countdown(work_seconds ,"Work time over , Time for Break!")
        playsound(r'D:\CODE\Python\Basic-projects\alarm_sound.mp3')

        countdown(break_seconds ,"Break time over , Time for Work!")
        playsound(r'D:\CODE\Python\Basic-projects\alarm_sound.mp3')

    print("All Pomodoro cycles complete!")

if __name__ == "__main__":
    main()