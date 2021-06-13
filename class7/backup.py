#!/usr/bin/env python

# Import libraries
import xmltodict
from pprint import pprint

# Exercise 3c function
# Create a function to open and parse xml files, but force the use of lists
def force_xml_list(filename):
    # Function to open and parse xml files, but force the use of lists 

    with open (filename) as f:
        xmldata = f.read().strip()

    force_xml_dict = xmltodict.parse(xmldata, force_list={'zones-security': True})
    return(force_xml_dict)


# Exercise 3a
# Create function to open and parse files to a varible using xmltodict
def parse_xmltodict(filename):
    # Reads file and parses using xmltodict, returns as a varible

    with open (filename) as f:
        xmldata = f.read().strip()

    xml_dict = xmltodict.parse(xmldata)
    return(xml_dict)

sh_zones = parse_xmltodict('show_security_zones.xml')
sh_zones_trust = parse_xmltodict('show_security_zones_trust.xml')

print('\nVarible No1:')
print('--------------\n')
pprint(sh_zones)
print('\n\n')

print('\nVarible No2:')
print('--------------\n')
pprint(sh_zones_trust)
print('\n\n')

# Exercise 3b
# Compare data type of the elements at ['zones-information']['zones-security']
print('\nVarible No1 Type:')
print('--------------\n')
print(type(sh_zones['zones-information']['zones-security']))
print('\n\n')

print('\nVarible No2 Type:')
print('--------------\n')
print(type(sh_zones_trust['zones-information']['zones-security']))
print('\n\n')


## Exercise 3c
## Print the data type and structure of 'my_xml'
sh_zones = force_xml_list('show_security_zones.xml')
sh_zones_trust = force_xml_list('show_security_zones_trust.xml')

print('\nVarible No1:')
print('--------------\n')
pprint(sh_zones)
print('\n\n')

print('\nVarible No2:')
print('--------------\n')
pprint(sh_zones_trust)
print('\n\n')

# Exercise 3b
# Compare data type of the elements at ['zones-information']['zones-security']
print('\nVarible No1 Type:')
print('--------------\n')
print(type(sh_zones['zones-information']['zones-security']))
print('\n\n')

print('\nVarible No2 Type:')
print('--------------\n')
print(type(sh_zones_trust['zones-information']['zones-security']))
print('\n\n')
