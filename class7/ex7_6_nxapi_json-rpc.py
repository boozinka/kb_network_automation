#!/usr/bin/env python

# Import libraries (requests imported to handle self signed cert warning)
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from nxapi_plumbing import Device
from getpass import getpass
from pprint import pprint

# Pass target device parameters through 'Device' to connect via API
device = Device(
    api_format = 'jsonrpc',
    host = 'nxos1.lasthop.io',
    username = 'pyclass',
    password = getpass(),
    transport = 'https',
    port = '8443',
    verify = False,
)

# Pass show command to device and assign output to varible
output = device.show('show interface ethernet1/1')

# Peel back data structure (dict) until we reach the interface attributes
output = output['TABLE_interface']['ROW_interface']

# Print the attributes we are interested in
intf = output['interface']
state = output['state']
mtu = output['eth_mtu']
print(f"\nInterface: {intf}; State: {state}; MTU: {mtu}\n")

