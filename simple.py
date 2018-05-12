from http.server import BaseHTTPRequestHandler, HTTPServer

import process
import sys

#############################################

bp = None

def startbot():
    global bp    
    if not ( bp is None):
        return("bot already running")
    else:        
        bp = process.PopenProcess(["python","lichess-bot.py"],"lichess-bot")            
        return("starting bot")

def stopbot():
    global bp
    if not ( bp is None):        
        bp.send_line("x")        
        bp = None    
        return("stopping bot")
    else:
        return("bot already stopped")

#############################################
 
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
        message = "nop"

        if self.path == "/b":
            message = startbot()            

        if self.path == "/s":
            message = stopbot()

        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return


def run():
  # Start server
  print('starting server...')
 
  server_address = ('localhost', int(sys.argv[1]))
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)

  print('running server on address',server_address)

  httpd.serve_forever()
 
 
run()
