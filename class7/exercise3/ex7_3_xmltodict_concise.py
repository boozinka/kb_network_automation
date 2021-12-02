#!/usr/bin/env python

# Import libraries
import xmltodict
from pprint import pprint

def parse_xmltodict(filename, tag=None):
    # Reads file and parses using xmltodict, returns as a varible

    with open (filename) as f:
        xmldata = f.read().strip()

    if not tag:
        xml_dict = xmltodict.parse(xmldata)
    else:
        xml_dict = xmltodict.parse(xmldata, force_list={tag: True})

    return(xml_dict)

filename1 = 'show_security_zones.xml'
filename2 = 'show_security_zones_trust.xml'


# Exercise 3a
# Create function to open and parse files to a varible using xmltodict
sh_zones = parse_xmltodict(filename1)
sh_zones_trust = parse_xmltodict(filename2)

print('\nEXERCISE 3a')
print('--------------\n')
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
print('\nEXERCISE 3b')
print('--------------\n')
print('\nVarible No1 Type:')
print('--------------\n')
print(type(sh_zones['zones-information']['zones-security']))
print('\n\n')

print('\nVarible No2 Type:')
print('--------------\n')
print(type(sh_zones_trust['zones-information']['zones-security']))
print('\n\n')


# Exercise 3c
# Force the parse to create list for defined data tags
sh_zones = parse_xmltodict(filename1)
sh_zones_trust = parse_xmltodict(filename2, 'zones-security')

print('\nEXERCISE 3c')
print('--------------\n')
print('\nVarible No1:')
print('--------------\n')
pprint(sh_zones)
print('\n\n')

print('\nVarible No2:')
print('--------------\n')
pprint(sh_zones_trust)
print('\n\n')

print('\nVarible No1 Type:')
print('--------------\n')
print(type(sh_zones['zones-information']['zones-security']))
print('\n\n')

print('\nVarible No2 Type:')
print('--------------\n')
print(type(sh_zones_trust['zones-information']['zones-security']))
print('\n\n')
