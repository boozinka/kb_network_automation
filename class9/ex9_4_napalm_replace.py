#!/usr/bin/env python

from my_functions import napalm_conn, create_checkpoint 
from my_devices import nxos1
from pprint import pprint

# Exercise 4b
# Call function to create a connection object 
device = napalm_conn(nxos1)

# Call function to retrieve a NXOS checkpoint and write it to a file 
checkpoint = create_checkpoint(device)

# Exercise 4d
# Stage and then discard the replace config comparing the diff's

# Create and assign filename to 'file_name'
host = device.hostname.split('.')
host = host[0]
file_name = host+'.checkpoint_replace'

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

# Close device connection gracefully
device.close()

