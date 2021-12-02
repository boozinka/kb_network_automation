#!/usr/bin/env python

import os
import json
import requests
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning

# Disable warning from using unsigned certificate
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def ipaddr_print(response, msg):
    # Print the IP addresses in BASE_URL/ipam/ip-addresses/

    # Assign results to varible
    results = response.json()['results']

    # Print header
    print()
    print(msg)
    print('-'*80, '\n')

    # Iterate through the list of IP address and their attributes
    for ip_addr in results:
        # Print each IP address
        print('IP Address: {}'.format(ip_addr['address']))


# Define the base URL as a constant
BASE_URL = "https://netbox.lasthop.io/api/"

# Set the token based on the NETBOX_TOKEN environment varible
token = os.environ['NETBOX_TOKEN']

# Define the http headers
http_headers = {'Content-Type': 'application/json; version=2.4;'}
if token:
    http_headers['Authorization'] = 'Token {}'.format(token)

# Call "get" from the requests library to retrieve information
response = requests.get(f'{BASE_URL}ipam/ip-addresses/', headers=http_headers, verify=False)

# Print the list of IP addresses before making the HTTP POST
msg = ('All IP addresses in https://netbox.lasthop.io/api/ipam/ip-addresses/'
       ' before the HTTP DELETE are:'
)
ipaddr_print(response, msg)

# Define IP address "id's" to be deleted
ids = ['367']

# Iterate over ids
for id in ids:
    # Call "DELETE" from the results library to delete information (IP address)
    delete_resp = requests.delete(
        f'{BASE_URL}ipam/ip-addresses/{id}/', headers=http_headers, verify=False
    )

    # Confirm deletion
    if delete_resp.ok:
        print(f'Device id: {id} deleted successfully')
    else:
        print(f'There was an issue deleting device id: {id}')

# Call "get" from the requests library to retrieve information
response = requests.get(f'{BASE_URL}ipam/ip-addresses/', headers=http_headers, verify=False)

# Print the list of IP addresses before making the HTTP POST
msg = ('All IP addresses in https://netbox.lasthop.io/api/ipam/ip-addresses/'
       ' after the HTTP DELETE are:'
)
ipaddr_print(response, msg)

