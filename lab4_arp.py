import optparse
import scapy.all as scapy 

def ARP_send(ip):
    source_ip = ''
    source_mac = ''

# Creating ARP request 

    arp_request = scapy.ARP()
    arp_request.pdst = ip

    print(arp_request.summary())

# Creating Ethernet frame 

    broadcast = scapy.Ether()
    broadcast.dst = "ff:ff:ff:ff:ff:ff"

    print(broadcast.summary())

# Combining frame and ARP request

    arp_request_broadcast = broadcast/arp_request
    arp_request_broadcast.show()

# Send Packet and Receive Response

    answered, unanswered = scapy.srp(arp_request_broadcast, timeout = 2)

    for element in answered:
        source_ip = element[1].psrc
        source_mac = element[1].hwsrc

        print(f"IP Address: {source_ip}")
        print(f"Mac Address: {source_mac}")


if __name__ == "__main__":
    
    parser = optparse.OptionParser(description="ARP Packet Sending")
    parser.add_option("-i","--ip", dest="ip", help="Ip Address")
    
    (options, args) = parser.parse_args()
    
    if not options.ip:
        parser.error("Please provide the ip address")
    else:
        ARP_send(options.ip)



