#!/usr/bin/env python

import yaml
from pprint import pprint

device_list = [{
    'device_name': 'cisco4',
    'host': 'cisco4.blah.blah',
    'username': 'fred',
    'password': 'somepassword',
    'device_type': 'cisco_ios'
}, {
    'device_name': 'arista1',
    'host': 'arista1.blah.blah',
    'username': 'fred',
    'password': 'somepassword',
    'device_type': 'arista_eos'
}, {
    'device_name': 'nxos1',
    'host': 'nxos1.blah.blah',
    'username': 'fred',
    'password': 'somepassword',
    'device_type': 'cisco_nxos'
}, {
    'device_name': 'srx2',
    'host': 'srx2.blah.blah',
    'username': 'fred',
    'password': 'somepassword',
    'device_type': 'juniper_junos'
}]

pprint(device_list)

with open('lab_devices_yaml.txt', 'w') as file:
    yaml.dump(device_list, file, default_flow_style=False)

