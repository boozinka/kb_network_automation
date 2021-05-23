#!/usr/bin/env python

# SSH Connect Using Netmiko
#
# Makes an SSH connection using Netmiko

import re
from netmiko import Netmiko
from getpass import getpass
from pprint import pprint
from ciscoconfparse import CiscoConfParse

# Assign varibles
bgp_nei_list = []

# BGP config as a string
bgp_str = """
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
"""

# Assign varibles
bgp_peers_dict = {}

# Convert string into a list
bgp_list = bgp_str.splitlines()

# Feed config list into 'ciscoconfparse'
bgp_parsed = CiscoConfParse(bgp_list)

# Find all interfaces
bgp_nei = bgp_parsed.find_objects_w_child(parentspec=r'^\s+neighbor ',
                                          childspec=r'^\s+remote-as ')

# Loop through neighbor statements and their child lines
for neighbor in bgp_nei:
    nei_ipaddr = (neighbor.text).split()
    for child in neighbor.children:
        # Capture on child lines containing 'remote-as'
        if re.search(r'remote-as', child.text):
            bgp_as = (child.text).split()
            bgp_nei_list.append((nei_ipaddr[1], bgp_as[1]))

print()
print('BGP Peers:')
pprint(bgp_nei_list)
print()


