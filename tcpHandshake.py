from scapy.all import IP,TCP,send,RandShort,sr1
import socket
from sys import argv

script,dst_ip,dst_port = argv
src_port = RandShort()

def handshake(dst_ip,dst_port,src_port):
    #craft ip and tcp syn packets
    ip = IP(dst=dst_ip)
    syn = TCP(sport=src_port,dport=dst_port,flags="S",seq=100)
    #receive the ack packet
    syn_ack = sr1(ip/syn)
    #define the ack packet sequence number
    ack_seq = syn_ack.seq + 1
    #craft the ack packet
    ack = TCP(sport=src_port,dport=dst_port,flags="A",seq=syn_ack.ack,ack=ack_seq)
    send(ip/ack)

def connection(dst_ip,dst_port,src_port):
    #create a sock object
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(("",src_port))
    sock.connect_ex((dst_ip,dst_port))

    try:
        sock.sendall(b"GET / HTTP/1.1\r\nHost: 192.168.1.101\r\n\r\n")

        response = sock.recv(4096)
        print(response)
    finally:
        sock.close

handshake(dst_ip,dst_port,src_port)
connection(dst_ip,dst_port,src_port)