#!/usr/bin/env python

import requests
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning

# Disable warning from using unsigned certificate
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Define the base URL as a constant
BASE_URL = "https://netbox.lasthop.io/api/"

# Define the http headers
http_headers = {"accept": "application/json; version=2.4;"}

# Call "get" from the requests library
response = requests.get(f'{BASE_URL}dcim/', headers=http_headers, verify=False)

# Print the various attributes
print()
print('The JSON Response (child endpoints under DCIM) are:')
print('-'*53, '\n')
response_json = response.json()
pprint(response_json)
print()

