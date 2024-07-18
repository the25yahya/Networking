import socket
from sys import argv

script,target_host,target_port,data = argv

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.sendto(data,(target_host,target_port))

data,addr = sock.recvfrom(4096)

print(data)

