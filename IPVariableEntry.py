# Module to request and parse single IP or multiple IPs from user input

import re
import sys

# IP filtering regex
ip_locate = r"\b(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\b"

# Single IP Input
single_ip_input = input("Please provide the IP address: ")
single_ip_match = re.search(ip_locate, single_ip_input)
if not single_ip_match:
    print(f"IP address address not provided. Exiting script")
    sys.exit()
else:
    single_ip = single_ip_match.group()
    print(f"IP Address: " + single_ip)

# IP Address Input
ip_list_input = input("Please provide list of all IPs: ")
ip_list = re.findall(ip_locate, ip_list_input)
if not ip_list:
    print(f"IP Addresses not provided. Exiting script")
    sys.exit()
else:
    print("IP Addresses: " + ", ".join(ip_list))