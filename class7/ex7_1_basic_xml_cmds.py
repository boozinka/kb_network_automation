#!/usr/bin/env python
 
# Import libraries
from lxml import etree
from pprint import pprint

# Parse the xml file using etree
my_xml = etree.parse('show_security_zones.xml')

# Exercise 1a
# Print the varible and varible type
print()
print(my_xml)
print(type(my_xml))
print()

# Exercise 1b
# Convert element (my_xml) back to a string (byte string)
# Convert byte string to a unicode string and print
print(etree.tostring(my_xml).decode())
print()

# Exercise 1c
# Assign and print the root element
my_xml = my_xml.getroot()
print('\nThe root element is:')
print(my_xml)
# Print the root element tag
print('\nThe root element tag is:')
print(my_xml.tag)
print()

# Exercise 1d
# Print the first child of root via direct indices and getchildren()
print('\nPrint 1st childs tag via direct indices:', my_xml[0].tag)
print('\nPrint 1st childs tag via getchildren():', my_xml.getchildren()[0].tag)
print()

# Exercise 1e
# Assign varible to 1st child element of root and access its 1st childs text
trust_zone = my_xml[0]
print(f"Security Zone: {trust_zone[0].text}")
print()

# Exercise 1f
# Iterate through all child elements of trust_zone varible
# and print tag name for each child
for child in trust_zone:
    print(f"\n'trust_zone' child is: {child.tag}")


