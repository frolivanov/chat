import socket
sock = socket.socket()
sock.bind(('',9091))
sock.listen(1)