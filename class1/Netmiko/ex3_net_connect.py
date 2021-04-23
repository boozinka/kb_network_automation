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
    'device_type': 'cisco_nxos',
    'session_log': 'nxos1_log.txt',
    'command': 'show version'
}

nxos2 = {
    'host': 'nxos2.lasthop.io',
    'username': username,
    'password': password,
    'device_type': 'cisco_nxos',
    'session_log': 'nxos2_log.txt',
    'command': 'show run'
}

# Loop through each dictionary with ConnectHandler
for device in (nxos1, nxos2):
    command = device.pop('command')
    net_conn = ConnectHandler(**device)
    output = net_conn.send_command(command)
    print(output)

net_conn.disconnect

