import argparse
import optparse
import subprocess

def mac_spoofer(interface, mac):
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])
    print("MAC address changed successfully")
    
    
if __name__ == "__main__":
    
    #
    # Using argparse:
    #
    
    # parser = argparse.ArgumentParser(description="MAC Address Spoofer")
    # parser.add_argument("interface", help="Interface name")
    # parser.add_argument("mac", help="New MAC address")
    # args = parser.parse_args()
    
    # mac_spoofer(args.interface, args.mac)
    
    #
    # Using depreciated optparse:
    #
    
    parser = optparse.OptionParser(description="MAC Address Spoofer")
    parser.add_option("-i", "--interface", dest="interface", help="Interface name")
    parser.add_option("-m", "--mac", dest="mac", help="New MAC address")
    (options, args) = parser.parse_args()
    
    if not options.interface or not options.mac:
        parser.error("Please provide both interface name and MAC address")
    else:
        mac_spoofer(options.interface, options.mac)
