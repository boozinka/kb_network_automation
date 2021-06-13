#!/usr/bin/env python

# Import libraries
from lxml import etree
from pprint import pprint

# Parse the xml file using etree
def read_xml(filename):
    # Encoding in document forces the read to be binary
    with open(filename, "rb") as f:
        return etree.fromstring(f.read())

filename = 'show_version.xml'
my_xml = read_xml(filename)

# Exercise 5a
# Print out the the namespace map of this XML object
print('EXERCISE 5a')
print('------------\n')
print('Print out the the namespace map of this XML object')
print('-'*60, '\n')

for ns, url in my_xml.nsmap.items():
    print(f"{ns}: {url}")
print()


# Exercise 5b
# Convert element (my_xml) back to a string (byte string)
print('EXERCISE 5b')
print('------------\n')
print('Use the find() method to access the text of the "proc_board_id"',
       'element Serial No')
print('-'*80, '\n')
print(my_xml.find('.//{*}proc_board_id').text)
print()
