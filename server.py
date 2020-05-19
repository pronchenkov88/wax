from http.server import HTTPServer
from MyMethod import MyHandler
HOST_NAME = 'localhost' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 8080 # Maybe set this to 9000.
server_class = HTTPServer
httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()
print(MyHandler.data)

