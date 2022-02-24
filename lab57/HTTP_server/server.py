""" Example using http.server built-in module

	Reference :https://docs.python.org/3/library/http.server.html

"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import socket


script_path = os.path.dirname(os.path.realpath(__file__))
print(script_path)
class RequestHandler(BaseHTTPRequestHandler):
	def __init__(self,*args):
		print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
		self.root = f'{script_path}/front-end/'
		super().__init__(*args)

	def _set_response(self, status_code):
		self.send_response(status_code)
		self.send_header("Content-type", "text/html")
		self.send_header("Server", "My awasome server!!!")
		self.send_header("AlaBala", "AlaBala VALue")
		self.end_headers()


	def do_GET(self):
		print(f'self.requestline: {self.requestline}')
		print(f'self.command: {self.command}')
		print(f'self.path: {self.path}')
		print(f'self.headers: {self.headers}')


		if self.path == '/':
			filename = self.root + 'index.html'
		else:
			filename = self.root + self.path

		with open(filename,'rb') as f:
			body = f.read()
			self.send_response(200)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			self.wfile.write(body)

	def do_POST(self):
		print('POST REQUEST RECIEVED')
		pass



if __name__ == "__main__":
	# create and run server on IP:posrt
	# addr = '127.0.0.1'

	SERVER_NAME = 'localhost'
	addr = socket.gethostbyname(SERVER_NAME)
	port = 8080

	server_address = (addr, port)

	httpd = HTTPServer(server_address, RequestHandler)

	print(f'Server is running {addr}:{port}')
	httpd.serve_forever()

