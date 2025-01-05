import scapy.all as scapy
import argparse

def arguments():
    args = argparse.ArgumentParser(description="ESCANER DE RED")
    args.add_argument("-t","--targert",required=True, dest="target", help="Target host ip or range")
    args.add_argument("-p","--port",required=True, dest="port", help="port o port range")
    args = args.parse_args()
    return args.target


def analizar_puerto():
    paquete = scapy.IP(dst="192.168.1.27")/scapy.TCP(dport=8080, flags='S')/'GET HTTP/1.0\r\n\r\n'
    resp = scapy.sr1(paquete, timeout=1, verbose=False)
    print(resp.getlayer(scapy.TCP).flags == 0x14) 
    print(resp.show())
    print(resp.getlayer(scapy.TCP).flags == 0x12) 

    #print(resp.show())
analizar_puerto()
