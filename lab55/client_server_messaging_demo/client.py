import socket

BUF_SIZE = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER_IP = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER_IP, PORT)

def send(msg):
    message = msg.encode(FORMAT)
    # msg_length = len(message)
    # send_length = str(msg_length).encode(FORMAT)
    # send_length += b' ' * (BUF_SIZE - len(send_length))
    # client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


# create an INET (i.e. IPv4), STREAMing (i.e. TCP) socket:
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# now connect to the server given with ADDR tupple:
client.connect(ADDR)
print(f'Client is connected to {ADDR} ')

# send some messages
send("Hello World!")

msg = input('Enter a message: ')
if msg:
    send(msg)
else:
    send(DISCONNECT_MESSAGE)