#!/usr/bin/env python

# ConnectHandler
from netmiko import ConnectHandler
from getpass import getpass

password = '88newclass'
username = 'pyclass'

# Create a dictionary of parameters to feed into 'ConnectHandler'
nxos1 = {
    'host': 'nxos1.lasthop.io',
    'username': username,
    'password': password,
    'device_type': 'cisco_nxos'
}

nxos2 = {
    'host': 'nxos2.lasthop.io',
    'username': username,
    'password': password,
    'device_type': 'cisco_nxos'
}

# Loop through each dictionary with ConnectHandler
for device in (nxos1, nxos2):
    net_conn = ConnectHandler(**device)
    print(net_conn.find_prompt())

net_conn.disconnect

