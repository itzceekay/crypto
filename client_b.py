# Python TCP Client B
import socket
import base64

host = socket.gethostname()
port = 2004
BUFFER_SIZE = 2000
MESSAGE = input("tcpClientB: Enter message/ Enter exit:")
msg  = base64.b64encode(bytes(MESSAGE, 'utf-8'))

tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientB.connect((host, port))

while msg != 'exit':
    tcpClientB.send(MESSAGE)
    data = base64.b64decode(tcpClientB.recv(BUFFER_SIZE)).decode('utf8')
    print(" Client received data:", data)
    MESSAGE = input("tcpClientB: Enter message to continue/ Enter exit:")
    msg = base64.b64encode(bytes(MESSAGE, 'utf-8'))


tcpClientB.close()
