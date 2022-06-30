import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("1", 5555))