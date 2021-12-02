#!/usr/bin/env python

# Import libraries
import xmltodict
from pprint import pprint

# Open the file and assign to a varible 
with open ('show_security_zones.xml') as f:
    xmldata = f.read().strip()

# Parse the xml file using xmltodict
xml_dict = xmltodict.parse(xmldata)

# Exercise 2a
# Print the data type and structure of 'my_xml'
print('\nEXERCISE 2A')
print('-------------')
print('\nData type is:', type(xml_dict))
print('\nThe xmltodict data structure is:\n')
pprint(xml_dict)

# Exercise 2b
# Print the names and an index number of each security zone in 'my_xml'
print('\nEXERCISE 2B')
print('-------------\n')

xml_list = xml_dict['zones-information']['zones-security']

for index, sz_dict in enumerate(xml_list, start=1):
    zonename = sz_dict['zones-security-zonename']
    print(f"Security Zone #{index}: {zonename}")
print()

