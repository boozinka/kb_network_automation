#!/usr/bin/env python

# Import pyeapi library
import pyeapi
from getpass import getpass
from pprint import pprint

# Define connection object
connection = pyeapi.client.connect(
    transport = 'https',
    host = 'arista3.lasthop.io',
    username = 'pyclass',
    password = getpass(),
    port = '443'
)

# Create 'pyeapi.client.node' object and pass in the 'connection'
device = pyeapi.client.Node(connection)
### Following used if enable password is required
# enable = getpass('Enable: ')
# device = pyeapi.client.Node(connection, enablepwd=enable)

# Issue show command via 'device' object pyeapi
output = device.enable('show ip arp')

# Peel back the complex data structure to access 'arp' details
arp_list = (output[0]['result']['ipV4Neighbors'])

# Iterate through the dictionaries, printing out the IP/arp mappings
for arp_dict in arp_list:
    print(f"Mapping: {arp_dict['address']} --> {arp_dict['hwAddress']}")

# Output results return the following
"""
[{'command': 'show ip arp',
  'encoding': 'json',
  'result': {'dynamicEntries': 5,
             'ipV4Neighbors': [{'address': '10.220.88.1',
                                'age': 0,
                                'hwAddress': '0062.ec29.70fe',
                                'interface': 'Vlan1, Ethernet1'},
                               {'address': '10.220.88.23',
                                'age': 0,
                                'hwAddress': '502f.a8b1.6900',
                                'interface': 'Vlan1, not learned'},
                               {'address': '10.220.88.34',
                                'age': 0,
                                'hwAddress': '00aa.7867.8f6b',
                                'interface': 'Vlan1, not learned'},
                               {'address': '10.220.88.37',
                                'age': 0,
                                'hwAddress': '0001.00ff.0001',
                                'interface': 'Vlan1, not learned'},
                               {'address': '10.220.88.38',
                                'age': 0,
                                'hwAddress': '0002.00ff.0001',
                                'interface': 'Vlan1, not learned'}],
             'notLearnedEntries': 4,
             'staticEntries': 0,
             'totalEntries': 5}}]
"""

