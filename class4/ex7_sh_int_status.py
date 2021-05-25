#!/usr/bin/env python

# Import TextFSM and Pretty Print
import textfsm
from pprint import pprint

# Assign varibles
intf_list = []

# Open the template file
template_file = 'ex2_show_int_status.tpl'
template = open(template_file)

# Read the output string in (config)
with open('ex1_show_int_status.txt') as f:
    raw_text_data = f.read()

# Parse the output string
reg_table = textfsm.TextFSM(template)
data = reg_table.ParseText(raw_text_data)

# Close the template file
template.close()

# Create a list of the headers/varibles in the template
my_headers = reg_table.header

# Zip the parsed data into a dictionary with my_headers as key & append to list
for interface in data:
    intf_dict = dict(zip(my_headers, interface))
    intf_list.append(intf_dict)

pprint(intf_list)

