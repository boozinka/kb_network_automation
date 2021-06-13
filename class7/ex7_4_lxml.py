#!/usr/bin/env python

# Import libraries
from lxml import etree
from pprint import pprint

# Parse the xml file using etree
my_xml = etree.parse('show_security_zones.xml')

# Exercise 4a
# Find first 'zones-security' and print tag, then print tag of all its children
print('\nEXERCISE 4a')
print('-------------\n')
sec_zone = my_xml.find('./zones-security')
print("Find the tag of the first 'zones-security' element")
print('-------------------------------------------------------\n')
print(sec_zone.tag)
print()
print("Find the tag of all child elements for 'zones-security'")
print('-------------------------------------------------------\n')
for child in sec_zone.getchildren():
    print(child.tag)
print()

# Exercise 4b
# Find first 'zones-security-zonename' and print that elements 'text'.
print('\nEXERCISE 4b')
print('-------------\n')
print("Find first 'zones-security-zonename' and print that elements 'text'")
print('-'*75, '\n')
print(my_xml.find('.//zones-security-zonename').text)
print()

# Exercise 4c
# Use the findall() method to find all occurrences of "zones-security".
# For each of these security zones, print out the security zone name
# ("zones-security-zonename", the text of that element) 
print('\nEXERCISE 4c')
print('-------------\n')
print("Find all 'zones-security' and print out the security zone name")
print('-'*75, '\n')
security_zones = my_xml.findall('./zones-security')
for element in security_zones:
    tag = element.find('./zones-security-zonename').tag
    text = element.find('./zones-security-zonename').text
    print(f"ZoneName: {tag} : {text}")
print()
