#!/usr/bin/env python
 
import json
import re
from pprint import pprint

# Create empty IPv4 and IPv6 lists
ipv4_list = []
ipv6_list = []

# Define IPv4 regular expression pattern
pattern = re.compile(r"\A(?:[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})?\Z")

# Read JSON file containing nxos interface data structure
with open("nxos_intf_json.txt") as file:
    intf_dict = json.load(file)


# Loop through interfaces with ip address dictionaries
for value in intf_dict.values():
    ipaddr_dict = value
    # Loop through IP address dictionary
    for value in ipaddr_dict.values():
        ip_details = value
        # Loop through IP addresses and associated Prefix lengths
        for key, value in ip_details.items():
            mask = next(iter(value.values()))     # Grab mask length
            ipv4 = re.match(pattern, key)         # check if IPv4 address
            if ipv4:
                ipv4_addr = key + '/' + str(mask) # Concatenate IP & Prefix
                ipv4_list.append(ipv4_addr)       # Append to IPv4 list
            else:
                ipv6_addr = key + '/' + str(mask)
                ipv6_list.append(ipv6_addr)

print()
pprint(ipv4_list)
print()
pprint(ipv6_list)
print()

"""
Alternative and more efficient way of doing it
"""

filename = "nxos_intf_json.txt"
with open(filename) as f:
    nxos_data = json.load(f)

ipv4_list = []
ipv6_list = []

for intf, ipaddr_dict in nxos_data.items():
    for ipv4_or_ipv6, addr_info in ipaddr_dict.items():
        for ip_addr, prefix_dict in addr_info.items():
            prefix_length = prefix_dict["prefix_length"]
            if ipv4_or_ipv6 == "ipv4":
                ipv4_list.append("{}/{}".format(ip_addr, prefix_length))
            elif ipv4_or_ipv6 == "ipv6":
                ipv6_list.append("{}/{}".format(ip_addr, prefix_length))

print("\nIPv4 Addresses: {}\n".format(ipv4_list))
print("\nIPv6 Addresses: {}\n".format(ipv6_list))


