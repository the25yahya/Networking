import socket
from scapy.all import * 
import threading

class tcpClient:
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.client = None
    def connect(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try : 
            self.client.connect((self.ip,self.port))
            print(f"[*] connected to {self.ip}:{self.port}")
        except socket.error as error:
            print(f"[*] error connecting to {self.ip}:{self.port} - {error}")
            self.client = None
    
    def send_request(self,data):
        if self.client:
            try:
                self.client.sendall(data.encode())
                print(f"[*] sent {data} to {self.ip}:{self.port}")
                response = self.client.recv(4096)
                print(response.decode())
            except socket.error as error:
                print(f"[*] error sending data : {error}")
        
        else:
            print(f"[*] not connected to {self.ip}:{self.port}")
    
    def close(self):
        if self.client:
          self.client.close()
          print(f"[*] connection to {self.ip}:{self.port} terminated")
          self.client=None


class tcpServer:
    def __init__(self,ip,port,clients=int) :
        self.ip = ip
        self.port = port
        self.clients = clients
    
    def server(self):
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((self.ip,self.port))
        server.listen(self.clients)
        print(f"[*] started tcp server at {self.ip}:{self.port}")


class udpClient:
    def __init__(self,ip,port) :
        self.ip = ip
        self.port = port
    



