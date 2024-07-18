import socket 
from sys import argv

script,target_host,target_port = argv


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((target_host,target_port))

request = f"GET / HTTP/1.1\r\nHost: {target_host}\r\n\r\n"

sock.send(request.encode("utf-8"))

response = sock.recv(4096)

print(response.decode("utf-8"))

