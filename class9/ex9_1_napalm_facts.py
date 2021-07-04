#!/usr/bin/env python

from napalm import get_network_driver
from my_devices import cisco3, arista1
from pprint import pprint

# Exercise 1b
# Open the napalm connection to the device and return the napalm connection object.
def napalm_conn(device):
   # Function open a napalm connection and return the connection object

    # Copy device to avoid modifying original copy and future 'pop' errors
    device = device.copy()
    # pop device type, as this is an invalid kwarg for napalm
    device_type = device.pop('device_type')
    # Identify underlying driver by passing the 'device_type'
    driver = get_network_driver(device_type)
    # Pass device to NAPALM with driver
    conn = driver(**device)
    # Open connection object
    conn.open()
    # Return connection object
    return conn 

print("\nThe 'cisco3' connection object is:", napalm_conn(cisco3))
print("\nThe 'arista1' connection object is:", napalm_conn(arista1))
print()


# Exercise 1c
# Create a list of NAPALM connection objects to 'cisco3' & 'arista1'
device_list = [cisco3, arista1]
conn_list = []

for device in device_list:
    conn_list.append(napalm_conn(device))
 

# Exercise 1d
# Iterate through the connection objects, print out the connection object
# in addition pretty print the facts for each device and also print out
# the device's NAPALM platform type (ios, eos et cetera).

for conn_obj in conn_list:
    print('\n\nConnection Object Is:', conn_obj) 
    print('\n')
    print('\nThe object facts are:\n\n')
    pprint(conn_obj.get_facts())
    print('\n\nThe object type is:', conn_obj.platform)

# Close all device connections
for device in conn_list:
    device.close()

