#!/usr/bin/env python

# Import pyeapi library
import ipdb
import pyeapi
from my_funcs import yaml_import
from os import sys
from getpass import getpass
from pprint import pprint

# Assign varibles
arp_dict = {}
device_arp_list = []

# import connection details/device from yaml file
my_devices = yaml_import('ex6_2_my_device.yml')

# Get the device password
pwd = getpass()

# Iterate through dictionaries (keys) in my_devices
for device_name, arp_values in my_devices.items():

    # Assign the device password to the dictionary
    arp_values['password'] = pwd
     
    # Create connection using 'pyeapi connect'
    connection = pyeapi.client.connect(**arp_values)

    # Create 'pyeapi.client.node' object and pass in the 'connection'
    device = pyeapi.client.Node(connection)

    # Issue show command via 'device' object pyeapi
    output = device.enable('show ip route')

    # Strip back data structure to access prefixes and their attributes
    route_dict = output[0]['result']['vrfs']['default']['routes']

    # Print header for display
    print()
    print(f"{'Route Type': <10}{'Prefix Address': >20}{'next-hop address': >18}")
    print('-'*50)
    print()

    # Iterate over prefixes and their attributes
    for prefix, attributes in route_dict.items():
        # Assign the 'route type' value
        route_type = attributes['routeType']
        # If it's a static route the find the next hop and print output
        if 'static' in route_type:
            next_hop = attributes['vias'][0]['nexthopAddr']
            print(f"{route_type: <10}{prefix: >20}{next_hop: >18}")
        # If not static then print output with the connected interface
        else:
            conn_intf = attributes['vias'][0]['interface']
            print(f"{route_type: <10}{prefix: >20}{conn_intf: >18}")
    print()


