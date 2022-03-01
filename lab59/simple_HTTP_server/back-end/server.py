import socket
import os
import re

PORT = 5050
SERVER_NAME = socket.gethostname()
SERVER_IP = socket.gethostbyname(SERVER_NAME)
BUF_SIZE = 1024
ENCODING = "utf-8"


# print(f' os.getcwd(): { os.getcwd()}')
SERVER_BASE_FOLDER = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
HTTPDOCS = SERVER_BASE_FOLDER+"/front-end"


def process_request(request):
	# ------------------------------- parse request ------------------------------ #
	request_lines = request.split('\n')
	first_line=request_lines[0].split()
	method=first_line[0]
	path=first_line[1]

	# ------------------------------- make response ------------------------------ #
	if path=='/':
		path="/index.html"

	# mimic that the server is setup to return files only from HTTPDOCS folder:
	resource_path = HTTPDOCS+path
	print(f'respurce_path: {resource_path}') # /front-end/index.html

	if method=="GET":
		if not os.path.exists(resource_path):
			status_line = "HTTP/1.1 404 Not Found\n"
			body=""
		else:
			with open(resource_path,'r') as fh:
				content = fh.read()
				status_line = "HTTP/1.1 200 OK\n"
				body = content


	if method=="POST":
		# get data from request body
		# EOL:
		# Windows: \r\n
		# Linux : \n
		# <acko
		data = re.split(r'(?:\r?\n){2}', request)[1]
		print(data)
		user_name=data.split("=")[1]

		# do something with data

		# return response
		status_line = "HTTP/1.1 200 OK\n"
		body = f"<h2>Welcome {user_name}</h2>"

	resp_headers = [
		f"Server: Fake Python Server",
		f"Content-Length:{len(body)}",
		f"Content-Type: text/html; charset=UTF-8"
	]
	response = status_line + "\n".join(resp_headers) + "\n\n" + body
	return response


# ----------------------- init server listening socket ----------------------- #
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER_IP, PORT))
s.listen()

print(f"Server is listening on {SERVER_IP}:{PORT}")

# ---------------------------- listen for clients ---------------------------- #
while True:
	(conn, addr) = s.accept()
	print(f'Client:{addr} connected!')

	# ----------------------- get client's request message: ---------------------- #
	msg_bytes = conn.recv(BUF_SIZE)
	request = msg_bytes.decode(ENCODING)

	print(f'request message: \n-->{request}<---\n ')

	# ----------------------- return HTTP formatted response ---------------------- #
	response = process_request(request)
	# print(f'RESPONSE:{response}')
	conn.send(response.encode(ENCODING))


	# ------------------------- close client's connection ------------------------ #
	conn.close()
	# if using HTTP1.1 and keep-alive header then make persistent connection



