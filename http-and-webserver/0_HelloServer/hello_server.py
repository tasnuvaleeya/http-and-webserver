from http.server import HTTPServer, BaseHTTPRequestHandler

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send a 200 Ok response
        self.send_response(200)

        # Then send Headers
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        
        
        # Write the response body
        self.wfile.write("Hello Http\n".encode())

if __name__ == '__main__':
    server_address = ('', 8080) # Server on all addresses port 8000
    httpd = HTTPServer(server_address, HelloHandler)
    httpd.serve_forever()