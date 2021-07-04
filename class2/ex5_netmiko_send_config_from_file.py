#!/usr/bin/env python
 
# SSH Connect Using Netmiko
#
# Makes an SSH connection using Netmiko

# ConnectHandler
from netmiko import Netmiko
from getpass import getpass
from pprint import pprint
from datetime import date, time, datetime

# Create dicionary of parameter to feed into 'net_connect'
nxos1 = {
    'host': 'nxos1.blah.blah',
    'username': 'fred',
    'password': 'somepassword',
    'device_type': 'cisco_nxos'
}

nxos2 = {
    'host': 'nxos2.blah.blah',
    'username': 'fred',
    'password': 'somepassword',
    'device_type': 'cisco_nxos'
}

# Assign varibles
sh_vlan = 'show vlan brief'

# Establish SSH Connection
net_conn = Netmiko(**nxos1)

# Send command down the channel to list before settings
print('#'*33, ' SETTINGS BEFORE CONFIG ', '#'*33)
print()
sh_vlan_brief = net_conn.send_command(sh_vlan)
pprint(sh_vlan_brief)

# Send commands down the channel in a for loop to configure device
cmds = net_conn.send_config_from_file(config_file='vlan_config.txt')
net_conn.save_config()
print(cmds)

# Send command down the channel to list before settings
print('#'*33, ' SETTINGS AFTER CONFIG ', '#'*33)
print()
sh_vlan_brief = net_conn.send_command(sh_vlan)
pprint(sh_vlan_brief)

net_conn.disconnect()

# Establish SSH Connection
net_conn = Netmiko(**nxos2)

# Send command down the channel to list before settings
print('#'*33, ' SETTINGS BEFORE CONFIG ', '#'*33)
print()
sh_vlan_brief = net_conn.send_command(sh_vlan)
pprint(sh_vlan_brief)

# Send commands down the channel in a for loop to configure device
cmds = net_conn.send_config_from_file(config_file='vlan_config.txt')
net_conn.save_config()
print(cmds)

# Send command down the channel to list before settings
print('#'*33, ' SETTINGS AFTER CONFIG ', '#'*33)
print()
sh_vlan_brief = net_conn.send_command(sh_vlan)
pprint(sh_vlan_brief)

net_conn.disconnect()
