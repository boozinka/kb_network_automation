#!/usr/bin/env python

import json
import re
from pprint import pprint

# Create empty arp dictionary
new_dict = {}

# Read JSON file containing Arista arp data structure
with open("arista_arp_json.txt") as file:
    arp_dict = json.load(file)

# Pop the dictionary element we are interested in
arp_list = arp_dict['ipV4Neighbors']

# Loop over dictionaries in the list
for arp_nei in arp_list:
    new_dict.update({arp_nei['address'] : arp_nei['hwAddress']})
print(new_dict)

