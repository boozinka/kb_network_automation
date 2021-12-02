#!/usr/bin/env python

import os
import json
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
http_headers = {'Content-Type': 'application/json; version=2.4;'}
if token:
    http_headers['Authorization'] = 'Token {}'.format(token)

# Define object id
id = '367'

# Define PUT data
put_data = {'address': '192.0.2.111/32',
            'description': 'WB-Ex11.5'
}

# Call "get" from the requests library to retrieve information
response = requests.put(f'{BASE_URL}ipam/ip-addresses/{id}/',
data=json.dumps(put_data), headers=http_headers, verify=False
)

# Print the response.json()
print()
print('JSON Response is:')
print('-'*30, '\n')
pprint(response.json())

# Print the Status Code
print()
print('Status Code is:')
print('-'*30, '\n')
pprint(response.status_code)
print()

