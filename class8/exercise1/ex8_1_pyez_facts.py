#!/usr/bin/env python

# Import libraries
from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

# Create an instance of device object
jnpr_dev = Device(host='srx2.lasthop.io', user='pyclass', password=getpass())

# Establish 'netconf' connection
jnpr_dev.open()

# Pretty print the devices facts
print()
print("Printing the devices 'facts'")
print('-'*30, '\n')
pprint(jnpr_dev.facts)
print()

# Print the devices 'facts' hostname
print()
print("Printing the devices 'facts' hostname")
print('-'*35, '\n')
print(f"Hostname: {jnpr_dev.facts['hostname']}")
print()
