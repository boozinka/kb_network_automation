#!/usr/bin/env python

from my_functions import napalm_conn, backup_config
from my_devices import cisco3, arista1
from pprint import pprint

# Exercise 2a
# Create a list of NAPALM connection objects to 'cisco3' & 'arista1'
device_list = [cisco3, arista1]
conn_list = []

for device in device_list:
    conn_list.append(napalm_conn(device))
 

# Exercise 2b
# Iterate through the connection objects, print out the arp table for each

for conn_obj in conn_list:
    print('\n\n', conn_obj.hostname, 'ARP Table')
    print('-'*30,'\n')
    pprint(conn_obj.get_arp_table())
    print()

# Exercise 2c
# Attempt to use the get_ntp_peers() method against both of the devices

for conn_obj in conn_list:
    print('\n\n', conn_obj.hostname, 'NTP Peers')
    print('-'*30,'\n')
    try:
        pprint(conn_obj.get_ntp_peers())
    except NotImplementedError:
        print("'get_ntp_peers' not implemented for",
              conn_obj.platform, "device type\n")

# Exercise 2d
# Get config of each device and write it to a separate file

# Iterate through the list of connection objects
for conn_obj in conn_list:

    # Call the function to back up the device running config to a file
    backup_config(conn_obj)

# Close all device connections down
for device in conn_list:
    device.close()
