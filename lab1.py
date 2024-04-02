import re
import subprocess
import sys

def get_whatweb_output(url):
    command = ["whatweb", url]
    try:
        output = subprocess.check_output(command, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return None


def clean_whatweb_output(output):
    # Regular expression pattern to extract information inside square brackets
    output = output.split(", ")
    ansi_escape = re.compile(r'\x1b\[([0-9]{1,2}(;[0-9]{1,2})?)?[mGK]')

    # Function to remove ANSI escape codes from a string
    def remove_escape_codes(s):
        return ansi_escape.sub('', s)

    # Apply the function to each element of the output list
    cleaned_output = [remove_escape_codes(entry) for entry in output]

    # Join the cleaned output list into a single string
    cleaned_output_str = ' '.join(cleaned_output)
    output2 = cleaned_output_str.split("' '")
    return output2

def check_wordpress(ilist):
    split_list = [item.split(" ") for item in ilist]
    new = split_list[0]
    found=False
    for item in new:
        if "WordPress" in str(item):
            found = True
    return found

def extract_info(input_list):
    http_server_info = None
    ip_address = None
    python_in = None

    http_server_regex = re.compile(r'HTTPServer\[(.*?)\]')
    ip_regex = re.compile(r'IP\[(.*?)\]')
    python_regex = re.compile(r'Python\[(.*?)\]')

    for item in input_list:
        
        http_server_match = http_server_regex.search(item)
        if http_server_match:
            http_server_info = http_server_match.group(1)

        ip_match = ip_regex.search(item)
        if ip_match:
            ip_address = ip_match.group(1)
        
        python_match = python_regex.search(item)
        if python_match:
            python_in = python_match.group(1)

    return http_server_info, ip_address, python_in

def single_mode(entry):
    name = entry
    output=[]
    apache = False
    wordpress = False
    apache_wordpress = False
    ip_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
    is_ip = re.match(ip_pattern, entry)
    
    if is_ip:
        url=None
        ip = entry
        wwo = get_whatweb_output(ip)
        cwwo = clean_whatweb_output(wwo)
        server, ipad, cpy = extract_info(cwwo)

    else:
        url= entry
        info = get_whatweb_output(entry)
        cwwo = clean_whatweb_output(info)
        server, ipad, cpy= extract_info(cwwo)

    if "Apache" in server:
        apache = True

    wordpress = check_wordpress(cwwo)
    
    if apache == True and wordpress == True:
        apache_wordpress = True

    output.append("URL: " + str(url))
    output.append("IP Address: " + str(ipad))
    output.append("Web Technologies: " + str(server))
    output.append("Python: " + str(cpy))
    output.append("Apache present: " + str(apache))
    output.append("Wordpress present: " + str(wordpress))
    output.append("Presence of both Apache and Wordpress: " + str(apache_wordpress))
    output.append("\n")

    nmap_command = f"nmap -p80 --script http-stored-xss.nse {ipad}"
    output.append("Executing nmap command: " + nmap_command)

    # Running the nmap command
    try:
        nmap_output = subprocess.check_output(nmap_command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        output.append(nmap_output)
    except subprocess.CalledProcessError as e:
        output.append("Error running nmap command: " + str(e))

    output.append("-"*100)

    # Write output to file
    with open("Reconnaissance_report_620147893.txt", "a") as file:
        for line in output:
            file.write(line + "\n")
    
    print(f"Reconnaisance report for {name} has been generated")

    
def batch_mode():
    filename = input("Enter the path to the text file containing URLs and IP addresses: ")
    
    try:
        with open(filename, "r") as file:
            entries = file.readlines()
    except FileNotFoundError:
        print("File not found. Please make sure you enter the correct path.")
        return
    
    for entry in entries:
        entry = entry.strip() 
        try:
            single_mode(entry)
        except Exception as e:
            print(f"Error processing entry '{entry}': {e}")
            continue 


def prompt():
    print("1. Single Entry Mode")
    print("2. Batch Mode")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        entry = input("Enter the IP address or URL: ")
        single_mode(entry)
    elif choice == '2':
        batch_mode()
    else:
        print("Invalid choice.")
        print("\n")
        prompt()


if __name__=="__main__":

    print("Warning: This tool is designed for informational purposes only. It is imperative to utilize this script responsibly and ethically, respecting the privacy and security of website owners. Any misuse, such as unauthorized probing or exploitation of vulnerabilities, is strictly prohibited and may result in legal consequences. Please exercise caution and ensure compliance with applicable laws and regulations when using this tool.")
    print("-"*100)
    prompt()


