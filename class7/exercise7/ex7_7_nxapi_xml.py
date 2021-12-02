#!/usr/bin/env python

# Import libraries (requests imported to handle self signed cert warning)
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lxml import etree
from nxapi_plumbing import Device
from getpass import getpass
from pprint import pprint

# Pass target device parameters through 'Device' to connect via API
device = Device(
    api_format = 'xml',
    host = 'nxos1.lasthop.io',
    username = 'pyclass',
    password = getpass(),
    transport = 'https',
    port = '8443',
    verify = False,
)

# Assign varibles
sh_cmds = ['show system uptime', 'show system resources']
config_cmds = ['interface loopback111', 'description WB-Loopback 111',
               'interface loopback112', 'description WB-Loopback 112'
]

# Exercise 7a
# Pass show command to device and assign output to varible
output = device.show('show interface ethernet1/1')

# Peel back data structure (dict) until we reach the interface attributes
output = output[0][0][0]

## Print the attributes we are interested in
intf = output.find('interface').text
state = output.find('state').text
mtu = output.find('eth_mtu').text
print('\nEXERCISE 7a')
print('\n------------\n')
print('Return an XML element and print the attributes we are interested in\n')
print(f"\nInterface: {intf}; State: {state}; MTU: {mtu}\n")
print()


# Exercise 7b
# Pass show commands to device and assign output to varible
output_list = device.show_list(sh_cmds)

# Print the attributes we are interested in
print('\nEXERCISE 7b')
print('\n------------\n')
print('Run "show system uptime" and "show system resources".',
      'Print the XML output from these two commands\n')
for xml in output_list:
    print(etree.tostring(xml).decode())
    input('Hit enter to continue: ')
print()


# Exercise 7c
# Pass config commands to device and assign output to varible
output_config = device.config_list(config_cmds)

# Verify and print the command outputs
print('\nEXERCISE 7c')
print('\n------------\n')
print('Configure two loopbacks on nxos1 including interface descriptions\n')
for xml_return in output_config:
    print()
    print(etree.tostring(xml_return).decode())
    input('\nHit enter to continue: ')
print()

