from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

# Global variable to store the current command
current_command = 'Write-Output "Hello from server"'

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        print(f"[-] Received GET request for {self.path}")  # Print statement for received GET request
        if self.path == '/script':
            print("[-] Serving the current command...")  # Before sending the command
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(current_command.encode())
            print(f"[+] Command sent: {current_command}")  # After sending the command
        else:
            print("[!] Received invalid GET request, sending 404...")  # For invalid GET paths
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        print(f"[-] Received POST request for {self.path}")  # Print statement for received POST request
        if self.path == "/endpoint":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode()       
            post_data = ''.join(post_data.split("=")[1])    
            print(f"[-] Received POST data: {post_data}")  # After receiving data
            print(f"[+] Output: {post_data}")  # Echoing the POST data
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"")
        else:
            print("[!] Received invalid POST request, no action taken.")  # For invalid POST paths

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=5005):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"[-] Starting httpd on port {port}...")  # Print statement for server start
    threading.Thread(target=httpd.serve_forever).start()
    print("[+] HTTP server is running in a separate thread.")  # After the server has started
    return httpd

def update_command():
    global current_command
    while True:
        command = input("Enter new command: ")
        print(f"[-] Updating command to: {command}")  # Before updating the command
        current_command = command
        print("[+] Command updated.")  # After updating the command


if __name__ == "__main__":
    print("[-] Starting the server and command update thread...")  # Initial print statement
    server = run()
    update_command_thread = threading.Thread(target=update_command)
    print("[+] Command update thread started.")  # After starting the thread
    update_command_thread.start()
