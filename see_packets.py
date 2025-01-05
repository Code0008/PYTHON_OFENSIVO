import scapy.all as scapy


def tratar_paquete(packet):
    print(packet.show())

def main():
    scapy.sniff(iface="ens33", prn= tratar_paquete, store=0)

if __name__ == "__main__":
    main()