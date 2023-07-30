from http.server import BaseHTTPRequestHandler, HTTPServer
import os

# Define the custom request handler
class FileUploadHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Handle GET requests here (if needed)
        pass

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        file_content = self.rfile.read(content_length)

        # Save the file content to a file (e.g., "uploaded_file.txt")
        with open("uploaded_file.txt", "wb") as file:
            file.write(file_content)

        # Send a response back to the client
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"File uploaded successfully.")

def run_server(server_address, handler_class):
    httpd = HTTPServer(server_address, handler_class)
    print(f"Server started on http://{server_address[0]}:{server_address[1]}")
    httpd.serve_forever()

if __name__ == '__main__':
    # Specify the server IP and port (localhost)
    server_address = ('', 80)  # Use an empty string for the IP to listen on all available interfaces

    # Start the server
    run_server(server_address, FileUploadHandler)
