# Sockets and Network Programming

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 4444))
message = s.recv(1024)
s.close()

print(message.decode())