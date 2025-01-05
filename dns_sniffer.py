import scapy.all as scapy

def process_dns_packet(packet):
    if packet.haslayer(scapy.DNSQR):
        dominio = packet[scapy.DNSQR].qname.decode()
        exclude_keywords = ["google", "cloud", "bing", "static"]
        if dominio not in dominios  and not any(keyword in dominio for keyword in exclude_keywords ):
            dominios.add(dominio)
            print(f"dominio: {dominio}")

        
def main():
    global dominios
    dominios = set()
    interface= "ens33"
    scapy.sniff(
                iface=interface,    # interfaz de red
                filter="udp and port 53", # filtro de re d 
                prn = process_dns_packet, # opoeracion que se hara al paquete
                store=0  # si se guarda en cache
                )

if __name__ =='__main__':
    main()