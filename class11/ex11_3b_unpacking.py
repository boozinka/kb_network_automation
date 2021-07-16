#!/usr/bin/env python

import os
import requests
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning

# Disable warning from using unsigned certificate
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Define the base URL as a constant
BASE_URL = "https://netbox.lasthop.io/api/"

# Set the token based on the NETBOX_TOKEN environment varible
token = os.environ['NETBOX_TOKEN']

# Define the http headers
http_headers = {"accept": "application/json; version=2.4;"}
http_headers['Authorization'] = f'Token {token}'

# Call "get" from the requests library
response = requests.get(f'{BASE_URL}dcim/devices/', headers=http_headers, verify=False)

# Print the "display_name" for each device 
device_list = response.json()['results']
for device in device_list:
    print()
    print('-'*60, '\n')
    print(device['display_name'])
    print('-'*15, '\n')
    print('Location: {}'.format(device['site']['name']))
    print('Vendor: {}'.format(device['device_role']['name']))
    print('Status: {}'.format(device['status']['label']))
    print('-'*60, '\n')

