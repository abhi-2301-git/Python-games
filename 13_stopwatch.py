import time
import threading
# i dont know the threading part it was done using chat gpt

def format_time(seconds):
    """Format seconds into hours, minutes, and seconds."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    return f"{hours}h {minutes}m {seconds:.2f}s"

def update_elapsed_time(running, start_time):
    """Function to continuously update and print elapsed time while running."""
    time.sleep(1)
    
    while running[0]:
        elapsed_time = (time.time() - start_time[0]) +1
        print(f"\rElapsed time: {format_time(elapsed_time)}", end='')  
        time.sleep(1)

def stopwatch():
    print("Stopwatch Program")
    print("Commands: 'start', 'stop', 'reset', 'exit'")

    start_time = [0]
    elapsed_time = [0]
    running = [False]

    while True:
        command = input("\nEnter command: ").strip().lower()

        if command == 'start':
            if not running[0]:
                start_time[0] = time.time() - elapsed_time[0]
                running[0] = True
                print("Stopwatch started") 
                print("Press 'stop' to stop, 'reset' to reset, or 'exit' to exit.")

                # Start the thread to update elapsed time
                threading.Thread(target=update_elapsed_time, args=(running, start_time), daemon=True).start()
            else:
                print("Stopwatch already running.")

        elif command == 'stop':
            if running[0]:
                elapsed_time[0] = time.time() - start_time[0]
                running[0] = False
                print(f"\nStopped at {format_time(elapsed_time[0])}.")
            else:
                print("Stopwatch is already stopped.")

        elif command == 'reset':
            if running[0]:
                elapsed_time[0] = time.time() - start_time[0]
                print(f"\nCurrent elapsed time before reset: {format_time(elapsed_time[0])}.")
            start_time[0] = 0
            elapsed_time[0] = 0
            running[0] = False
            print("Stopwatch has been reset.")

        elif command == 'exit':
            if running[0]:
                elapsed_time[0] = time.time() - start_time[0]
                print(f"\nExiting Stopwatch. Final elapsed time: {format_time(elapsed_time[0])}.")
            else:
                print("Exiting Stopwatch.")
            running[0] = False
            break

        else:
            print("Invalid command! Please enter 'start', 'stop', 'reset', or 'exit'.")

if __name__ == "__main__":
    stopwatch()