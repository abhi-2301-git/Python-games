import time

def disp_time():
    while True:
        current_time = time.strftime("%H:%M")
        print(current_time, end="\r")
        time.sleep(60)

if __name__ == "__main__":
    disp_time()