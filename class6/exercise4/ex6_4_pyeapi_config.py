#!/usr/bin/env python

# Import pyeapi and misc libraries
import ipdb
import pyeapi
from my_funcs import yaml_import
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from os import sys
from getpass import getpass
from pprint import pprint

# Set undefined = strict to pick up errors is varibles
env = Environment(undefined=StrictUndefined)
# Set template file location (sub-directory of pwd)
env.loader = FileSystemLoader('./templates')

# import connection details/device from yaml file
my_devices = yaml_import('ex6_4_my_devices.yml')

# Get the device password
pwd = getpass()

# Iterate through dictionaries in my_devices
for device_name, device_attr in my_devices.items():

    # Assign the device password to the dictionary
    device_attr['password'] = pwd

    # Pop the device configuration data in the form of a dictionary
    config_dict = device_attr.pop('data')

    # Generate the configuration using Jinja2 templating
    template_file = 'ex6_4_intf_config.j2'
    template = env.get_template(template_file)
    config_str = template.render(**config_dict)

    # Convert render output to a list of commands and strip whitespace
    cmd_list = []
    config_list = config_str.splitlines()
    for i in config_list:
        cmd_list.append(i.strip())

    # Create connection using 'pyeapi connect'
    connection = pyeapi.client.connect(**device_attr)

    # Create 'pyeapi.client.node' object and pass in the 'connection'
    device = pyeapi.client.Node(connection)

    # Issue configuration commands list via 'device' object pyeapi
    cmd_output = device.config(cmd_list)

    # Issue show command via 'device' object pyeapi
    sh_output = device.enable('show ip interface brief')
    result = sh_output[0]['result']['output']

    # Print the IP Address Table out
    device_name = device_name.capitalize()
    print()
    print(f"{device_name} IP Address Table")
    print('-'*80)
    print(result)
    print()

