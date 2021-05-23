#!/usr/bin/env python

import yaml
from pprint import pprint
from netmiko import ConnectHandler

# Read YAML file containing device structure
with open("lab_devices_yaml.txt") as file:
    device_list = yaml.load(file)

# Loop through each dictionary with ConnectHandler
for device in (device_list):
    device.pop('device_name')
    net_conn = ConnectHandler(**device)
    prompt = net_conn.find_prompt()
    print(prompt)

net_conn.disconnect

