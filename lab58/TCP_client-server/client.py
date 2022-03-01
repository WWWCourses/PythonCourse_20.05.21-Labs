from pydoc import cli
import socket

PORT = 5050
SERVER_NAME = 'localhost'
# SERVER_IP = socket.gethostbyname(SERVER_NAME)
SERVER_IP = '127.0.0.1'


# create an INET (i.e. IPv4), STREAMing (i.e. TCP) socket:
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# reuse address (optional, only for test purposes)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# now connect to the server given with (SERVER_IP, PORT) tupple:
client.connect((SERVER_IP, PORT))
print(f'Client is connected to {(SERVER_IP, PORT)} ')

client.send('hello'.encode('utf-8'))

client.close()