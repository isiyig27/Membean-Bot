from http.server import HTTPServer
from serverclass import RequestHandler
import threading
def run(server_class=HTTPServer, handler_class=RequestHandler, port=1050):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    #server_thread = threading.Thread(target=httpd.serve_forever)
    #server_thread.start()
    httpd.serve_forever()
run()