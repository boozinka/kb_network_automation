#!/usr/bin/env python

# SSH Connect Using Netmiko
#
# Makes an SSH connection using Netmiko

import re
from netmiko import Netmiko
from getpass import getpass
from pprint import pprint
from ciscoconfparse import CiscoConfParse

# Create dicionary of parameter to feed into 'net_connect'
cisco4 = {
    'host': 'cisco4.blah.blah',
    'username': 'fred',
    'password': 'somepassword',
    'device_type': 'cisco_ios',
}

# Assign varibles
sh_run = 'show run'
intf_dict = {}

# Establish SSH Connection
net_conn = Netmiko(**cisco4)

# Send command down the channel
print()
config = net_conn.send_command(sh_run)
net_conn.disconnect()

# Convert string into a list
config_list = config.splitlines()

# Feed config list into 'ciscoconfparse'
config_parsed = CiscoConfParse(config_list)

# Find all interfaces
intf = config_parsed.find_objects_w_child(parentspec=r'^interface',
                                          childspec=r'^\s+ip address ')

# Loop through interfaces and their child configs
for interface in intf:
    for child in interface.children:
        # if 'ip address' in child line then update the dictionary
        if re.search(r'ip address', str(child)):
            intf_dict.update({interface.text: child.text})

# Iterate through the dictionary printing the items
for cisco_intf, ip_addr in intf_dict.items():
    print()
    print('Interface Line: {}'.format(cisco_intf))
    print('IP Address Line: {}'.format(ip_addr))
    print()


