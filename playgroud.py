import Networking


server = Networking.tcpServer('127.0.0.1',5555,4)

server.start_server()