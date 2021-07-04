#!/usr/bin/env python
 
# ConnectHandler
from netmiko import ConnectHandler
from getpass import getpass

# Create a dictionary of parameters to feed into 'ConnectHandler'
my_device = {
    'host': 'nxos2.blah.net',
    'username': 'fred',
    'password': 'somepassword',
    'device_type': 'cisco_nxos'
}

# Make SSH connection
net_conn = ConnectHandler(**my_device)
print(net_conn.find_prompt())

net_conn.disconnect

