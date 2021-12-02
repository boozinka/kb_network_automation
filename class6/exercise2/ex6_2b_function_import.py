#!/usr/bin/env python

# Import pyeapi library
import ipdb
import pyeapi
from my_funcs import yaml_import, arp_out
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
    output = device.enable('show ip arp')

    # Access 'arp' details as a list in the data structure
    arp_list = (output[0]['result']['ipV4Neighbors'])

    # Create new dictionary with device name as key and arp list as value
    arp_dict = {device_name: arp_list}

    # Add the dictionary to create a list of devices with their arp mappings
    device_arp_list.append(arp_dict)
    
# Call function to print out devices and associated arp values
arp_out(device_arp_list)



