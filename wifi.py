from scapy.all import sendp,sniff,RadioTap,Dot11,Dot11ProbeReq,Dot11ProbeResp
import os

def handle_probe_response(pkt):
    if pkt.haslayer(Dot11ProbeResp):
        ssid = pkt.info.decode()
        bssid = pkt.addr3
        print(f"SSID: {ssid}, BSSID: {bssid}")

try:
    os.system("iwconfig eth0 mode monitor")
    sniff(prn=handle_probe_response,iface="eth0",lfilter=lambda x: x.haslayer(Dot11ProbeResp))


except PermissionError:
    print("Attention, are you root !?? :)")
