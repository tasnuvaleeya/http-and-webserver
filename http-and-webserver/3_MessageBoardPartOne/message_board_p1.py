from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 1. How long was the message? (Use the Content-Length header.)
        length = int(self.headers.get('Content-Length', 0))
        # 2. Read the correct amount of data from the request.
        data = self.rfile.read(length).decode()
        # 3. Extract the "message" field from the request data.
        message = parse_qs(data)["message"][0]

        # Send the "message" field back as the response.
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode())

if __name__ == '__main__':
    server_address = ('', 8088)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()