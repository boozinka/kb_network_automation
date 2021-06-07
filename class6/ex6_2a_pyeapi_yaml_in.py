#!/usr/bin/env python

# Import pyeapi library
import ipdb
import yaml
import pyeapi
from os import sys
from getpass import getpass
from pprint import pprint

#ipdb.set_trace()

# import connection details/device from yaml file
with open('ex6_2_my_device.yml') as f:
    my_devices = yaml.load(f)

# Assign 'arista4' dictionary to 'my_device'
my_device = my_devices['arista4']

# Get the device password and assign it to the dictionary
pwd = getpass()
my_device['password'] = pwd

# Create connection using 'pyeapi connect'
connection = pyeapi.client.connect(**my_device)

# Create 'pyeapi.client.node' object and pass in the 'connection'
device = pyeapi.client.Node(connection)

# Issue show command via 'device' object pyeapi
output = device.enable('show ip arp')

# Peel back the complex data structure to access 'arp' details
arp_list = (output[0]['result']['ipV4Neighbors'])

# Iterate through the dictionaries, printing out the IP/arp mappings
for arp_dict in arp_list:
    print(f"Mapping: {arp_dict['address']} --> {arp_dict['hwAddress']}")

