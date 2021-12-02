#!/usr/bin/env python

import requests
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning

# Disable warning from using unsigned certificate
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Define the base URL
url = "https://netbox.lasthop.io/api/"

# Call "get" from the requests library
response = requests.get(url, verify=False)

# Print the various attributes
print()
print('The HTTP Status Code is:')
print('-'*30, '\n')
json_status_code = response.status_code
pprint(json_status_code)
print()
print('The Response Text is:')
print('-'*30, '\n')
json_text = response.text
pprint(json_text)
print()
print('The JSON Response is:')
print('-'*30, '\n')
response_json = response.json()
pprint(response_json)
print()
print('The HTTP Response Headers are:')
print('-'*32, '\n')
json_headers = response.headers
pprint(dict(json_headers))
print()

