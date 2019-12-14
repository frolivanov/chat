import socket
sock = socket.socket()
sock.bind(('',9092))
sock.listen(3)