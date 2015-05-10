#this is a python server
import sys
import BaseHTTPServer
import SimpleHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
   def do_POST(self):
   	   print "In the do get function"
       # Parse query data & params to find out what was passed
       #parsedParams = urlparse.urlparse(self.path)
       #queryParsed = urlparse.parse_qs(parsedParams.query)
      
       # request is either for a file to be served up or our test
       #if parsedParams.path == "/test":
         # self.processMyRequest(queryParsed)
       #else:
          # Default to serve up a local file 
         # SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self);

print "start server"

HandlerClass = MyHandler
ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = "HTTP/1.0"

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000
server_address = ('127.0.0.1', port)

HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)

sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."


httpd.serve_forever()