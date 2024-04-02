import subprocess
import re

def run_nmap_scan(ip_address):
    try:
        # Run Nmap scan and capture output
        output = subprocess.check_output(['nmap', '-sn', ip_address])

        # Convert output to string
        output = output.decode('utf-8')

        # Check if host is up
        is_host_up = re.search(r'Host is up', output) is not None

        # Check if ports 80 or 443 are open
        ports_open = re.search(r'(80|443)/tcp\s+open', output) is not None

        # Count number of hosts on the network
        num_hosts = re.findall(r'(\d+) hosts up', output)
        num_hosts = int(num_hosts[0]) if num_hosts else 0

        # Extract MAC address for each host
        mac_addresses = re.findall(r'MAC Address: ([^\s]+)', output)

        return {
            'IP Address': ip_address,
            'Host Up': is_host_up,
            'Port 80 or 443 Open': ports_open,
            'Number of Hosts on Network': num_hosts,
            'MAC Addresses': mac_addresses
        }
    except subprocess.CalledProcessError:
        return None

def main():
    # Define list of IP addresses
    ip_addresses = ['137.74.187.100']

    # Iterate over IP addresses and run Nmap scan
    for ip_address in ip_addresses:
        result = run_nmap_scan(ip_address)
        if result:
            print("Results for IP Address:", ip_address)
            print("Host Up:", result['Host Up'])
            print("Port 80 or 443 Open:", result['Port 80 or 443 Open'])
            print("Number of Hosts on Network:", result['Number of Hosts on Network'])
            print("MAC Addresses:", result['MAC Addresses'])
            print()

if __name__ == "__main__":
    main()

