# BasicKeyloggers
Here I have some examples of keyloggers I've made just for fun.

# keylogger1
This is just a keylogger that saves the file in the same machine. Something very basic and simple

# keyloggerToMachine
Sends the all the logged information to a machine to specify in the code. On the send_file() function, you have to specify the IP and the port you want to send it.

In my case, I checked everything setting up a listener using netcat "netcat -nvlp 3333". When finishing the writing, just press CTRL+C and the files will be send automatically to the specified IP and port.

# KeyloggerToWebServer
I have here 2 python files.

The first one is the server. This is just a server that supports POST requests (to upload the keylogger file) and saves the file uploaded with the name "uploaded_file.txt"

Then, the second one is a keylogger that saves the info including a timestamp (showed each time "enter" is pressed) and ends with CTRL+C. 
It detects some special keys such as spaces and backspaces (just to meke it more readable). 
Also the program has a "capture_screenshot" function using the pyautogui module.
It has error handling on the last two functions and it has a timer between captured screenshots.

