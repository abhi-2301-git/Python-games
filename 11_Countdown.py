import time
import threading
def countdown(count_sec):
    while count_sec > 0:
        mins , sec = divmod(count_sec , 60)
        format = f"{mins:02}:{sec:02}"
        print( format , end="\r")
        time.sleep(1)
        count_sec -=1
    print('Times Up!')

def main():
    count_sec = int(input("Enter the countdown time in s: "))
    timer_thread = threading.Thread(target=countdown, args=(count_sec,))
    timer_thread.start()

if __name__ == "__main__":
    main()