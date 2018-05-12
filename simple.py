from http.server import BaseHTTPRequestHandler, HTTPServer

import process
import sys

bp = None

def startbot():
    global bp
    print("starting bot")
    if not ( bp is None):
        print("bot already running")
    else:
        bp = process.PopenProcess(["python","lichess-bot.py"],"lichess-bot")    
        print("bot process started",bp)

def stopbot():
    global bp
    print("stopping bot")    
    if not ( bp is None):
        bp.send_line("x")
        print("bot process stopped")
        bp = None    
    else:
        print("no bot running")    
 
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        # Send message back to client
        message = "Hello world!"

        if self.path == "/b":
            startbot()
            message = "bot start received"

        if self.path == "/s":
            stopbot()
            message = "bot stop received"

        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return
 
def run():
  print('starting server...')
 
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('', int(sys.argv[1]))  
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server on address',server_address)
  httpd.serve_forever()
 
 
run()