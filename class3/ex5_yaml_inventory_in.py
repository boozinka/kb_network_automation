#!/usr/bin/env python

import yaml
from pprint import pprint
from netmiko import ConnectHandler

# Read YAML file containing device structure
with open(".netmiko.yml") as file:
    device_list = yaml.load(file)

for device_group in ['cisco', 'nxos', 'arista', 'juniper']:
    group_list = device_list[device_group]
    for device in group_list:
        host = device_list[device]
        net_conn = ConnectHandler(**host)
        prompt = net_conn.find_prompt()
        print(prompt)
        net_conn.disconnect


