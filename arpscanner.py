import scapy.all as scapy
import argparse


def get_argument():
    parser = argparse.ArgumentParser(description="ARP escaner con scapy")
    parser.add_argument("-t","--targert",required=True, dest="target", help="Target host ip or range")
    args = parser.parse_args()
    return args.target

def scan(target):
    # arp.arping
    arp_packet =  scapy.ARP(pdst=target) #construimos el paquete arp
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #192.168.1.0/24
    arp_packet = broadcast_packet/arp_packet
    # / nos permite en terminos de redes unir capas o protocolos de red
    resp, unresp =scapy.srp(arp_packet, verbose=False, timeout = 1)
    if resp:
        print(resp)



def main():
    target = get_argument()
    scan(target)

if __name__ == '__main__':
    main()