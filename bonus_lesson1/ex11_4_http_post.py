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
http_headers = {'accept': 'application/json; version=2.4;',
                'Content-Type': 'application/json; version=2.4;'
}
if token:
    http_headers['Authorization'] = 'Token {}'.format(token)

# Define JSON payload
post_data = {'address': '192.0.2.113/32'}

# Call "get" from the requests library to retrieve information
response = requests.get(f'{BASE_URL}ipam/ip-addresses/', headers=http_headers, verify=False)

# Print the list of IP addresses before making the HTTP POST
msg = ('All IP addresses in https://netbox.lasthop.io/api/ipam/ip-addresses/'
       ' before the HTTP POST are:'
)
ipaddr_print(response, msg)

# Call "POST" from the results library to add information (IP address)
add_response = requests.post(
    f'{BASE_URL}ipam/ip-addresses/', headers=http_headers,
      data=json.dumps(post_data), verify=False
)

# Return response code
print()
print('Creating IP address object:')
print(f'Response Code: {add_response}\n')
print('Returned JSON:')
print('-'*35, '\n')
pprint(add_response.json())

# Retrieve the new object id
print()
print('Query newly created object...')
addr_id = add_response.json()['id']

# Form new URL specific to our new device object
url = f'{BASE_URL}ipam/ip-addresses/{addr_id}/'
id_resp = requests.get(url, headers=http_headers, verify=False)
print()
print('-'*35, '\n')
pprint(id_resp.json())

# Print the list of IP addresses after making the HTTP POST
response = requests.get(f'{BASE_URL}ipam/ip-addresses/', headers=http_headers, verify=False)
msg = ('All IP addresses in https://netbox.lasthop.io/api/ipam/ip-addresses/'
       ' after the HTTP POST are:'
)
ipaddr_print(response, msg)

