import subprocess
import os
import argparse

# Function to retrieve the current MAC address
def get_mac_address(interface):
    try:
        output = subprocess.check_output(["ifconfig", interface])
        mac_address_index = output.decode().split().index("ether") + 1
        mac_address = output.decode().split()[mac_address_index]
        return mac_address
    except Exception as e:
        print("Error:", e)
        return None

# Function to read the previously stored MAC address
def read_stored_mac_address(file_path):
    try:
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                return file.readline().strip()
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None

# Function to compare current and stored MAC addresses
def check_mac_address_changed(interface, stored_mac_address):
    current_mac_address = get_mac_address(interface)
    if current_mac_address:
        if stored_mac_address:
            if current_mac_address != stored_mac_address:
                print("MAC address has been changed!")
            else:
                print("MAC address has not been changed.")
        else:
            print("No stored MAC address found.")
    else:
        print("Failed to retrieve current MAC address.")

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Check if the MAC address of a specified interface has been changed.")
    parser.add_argument("interface", help="Name of the interface (e.g., eth0, wlan0)")
    args = parser.parse_args()

    # Interface name
    interface = args.interface

    # File path to store the previous MAC address
    file_path = "stored_mac_address.txt"

    # Read the previously stored MAC address
    stored_mac_address = read_stored_mac_address(file_path)

    # Check if MAC address has changed
    check_mac_address_changed(interface, stored_mac_address)

    # Store the current MAC address for future comparison
    current_mac_address = get_mac_address(interface)
    if current_mac_address:
        with open(file_path, "w") as file:
            file.write(current_mac_address)
    else:
        print("Failed to store current MAC address.")

