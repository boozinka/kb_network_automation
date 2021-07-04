#!/usr/bin/env python
 
# SSH Connect Using Netmiko
#
# Makes an SSH connection using Netmiko

# ConnectHandler
from netmiko import Netmiko
from getpass import getpass
from pprint import pprint

# Create dicionary of parameter to feed into 'net_connect'
cisco4 = {
    'host': 'cisco4.blah.blah',
    'username': 'fred',
    'password': 'somepassword',
    'device_type': 'cisco_ios'
}

# Establish SSH Connection
net_conn = Netmiko(**cisco4)

# Send command down the channel, expecting raw output
sh_ver = net_conn.send_command('sh ver', use_textfsm=True)
print('\nShow Version Output Type = ', type(sh_ver))
print('\n')
pprint(sh_ver)

# Send command down the channel and parse through TextFSM
sh_lldp = net_conn.send_command('show lldp neighbors', use_textfsm=True)
print('\nShow LLDP Output Type = ', type(sh_lldp))
print('\n')
pprint(sh_lldp)


# Extract Remote Port id
print('\nRemote Port id is:', sh_lldp[0]['neighbor_interface'])
print()

net_conn.disconnect()
