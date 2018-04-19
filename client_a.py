# Python TCP Client A
import socket
import base64

host = socket.gethostname()
port = 2004
BUFFER_SIZE = 2000
MESSAGE = input("tcpClientA: Enter message/ Enter exit:")
msg  = base64.b64encode(bytes(MESSAGE, 'utf-8'))

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientA.connect((host, port))

while msg != 'exit':
    tcpClientA.send(msg)
    data = base64.b64decode(tcpClientA.recv(BUFFER_SIZE))
    print(" Client2 received data:", data)
    MESSAGE = input("tcpClientA: Enter message to continue/ Enter exit:")
    msg = base64.b64encode(bytes(MESSAGE, 'utf-8'))

tcpClientA.close()