import socket
import threading

BUFF_SIZE = 4096
FORMAT = 'utf-8'
DISCONNECT_MESSAGE='close'

def handle_client(conn, addr):
	print(f"[NEW CONNECTION] {addr} connected.")
	connected = True

	while connected:
		msg = conn.recv(BUFF_SIZE)

		if msg == DISCONNECT_MESSAGE or not msg:
			break

		# conn.send("Msg received".encode(FORMAT))
		print("Msg received".encode(FORMAT))

	conn.close()

PORT = 5050
# SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_IP = '127.0.0.1'
print(socket.gethostname())

# create an INET (i.e. IPv4), STREAMing (i.e. TCP) socket:
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# reuse address (optional, only for test purposes)
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind the socket to the host
server.bind((SERVER_IP, PORT))

server.listen()
print(f"Server is listening on {SERVER_IP}")


while True:
	conn, addr = server.accept()
	# better to do with threading
	handle_client(conn, addr)

	print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")