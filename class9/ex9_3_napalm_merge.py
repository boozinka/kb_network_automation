#!/usr/bin/env python

from my_functions import napalm_conn, backup_config
from my_devices import cisco3, arista1
from pprint import pprint

# Exercise 3a
# Create a list of NAPALM connection objects to 'cisco3' & 'arista1'
device_list = [cisco3, arista1]
conn_list = []

for device in device_list:
    conn_list.append(napalm_conn(device))
 

# Exercise 3b
# Use load_merge_candidate() & loopback confi file to stage a config change
# Use the NAPALM compare_config() method to print out the pending differences

for device in conn_list:
    # Create and assign filename to 'file_name'
    file_name = device.hostname+'-loopbacks'

    # Stage candidate configuration and print diff
    print('\n\nStaging candidate configuration for',device.hostname)
    print('-'*60, '\n')
    device.load_merge_candidate(file_name)
    print('------ DIFF BEGIN ------\n')
    print(device.compare_config())
    print('\n------ DIFF END ------\n')

    # Discard candidate configuration and print diff
    print('\n\nDiscarding Candidate Configuration for', device.hostname)
    print('-'*60, '\n')
    device.discard_config()
    print('------ DIFF BEGIN ------\n')
    print(device.compare_config())
    print('\n------ DIFF END ------\n')

    # Re-stage candidate configuration and print diff
    print('\n\nRe-staging candidate configuration for',device.hostname)
    print('-'*60, '\n')
    device.load_merge_candidate(file_name)
    print('------ DIFF BEGIN ------\n')
    print(device.compare_config())
    print('\n------ DIFF END ------\n')

    # Exercise 3c
    # Commit candidate configuration and print diff
    print('\n\nCommited candidate configuration for',device.hostname)
    print('-'*60, '\n')
    device.commit_config()
    print('------ DIFF BEGIN ------\n')
    print(device.compare_config())
    print('\n------ DIFF END ------\n')

    # Rollback candidate configuration and print diff
    print('\n\nRolled back configuration for',device.hostname)
    print('-'*60, '\n')
    device.rollback()
    print('------ DIFF BEGIN ------\n')
    print(device.compare_config())
    print('\n------ DIFF END ------\n')

# Close all device connections
for device in conn_list:
    device.close()

