#!/usr/bin/env python
 
from pprint import pprint

arp_str = """
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
"""

# Strip "\n" from 1st line
arp_str = arp_str.strip()

# Split string in list based on "\n"
arp_list = arp_str.splitlines()

# Create empty list to append the dictionaries to
arp_output = []

# loop through the list
for i in arp_list:
    if "Protocol" in i:  # Skip the header
        continue
    else:
        line = i.split()
        arp_dict = {
            'mac_addr': line[3],
            'ip_addr': line[1],
            'intf': line[5]
}
        arp_output.append(arp_dict)

pprint(arp_output)



