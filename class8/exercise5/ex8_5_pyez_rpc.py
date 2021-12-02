#!/usr/bin/env python

from jnpr.junos import Device
from jnpr_devices import srx2
from getpass import getpass
from pprint import pprint
from lxml import etree

# Instantiate a NETCONF connection to the Juniper SRX2
jnpr_dev = Device(**srx2)
jnpr_dev.open()

# show version | display xml rpc
# <get-software-information>
#ver_xml = jnpr_dev.rpc.get_software_information()
#print(etree.tostring(ver_xml, pretty_print=True, encoding='unicode'))


# show interfaces terse | display xml rpc
# <get-interface-information>
#        <terse>
intf_xml = jnpr_dev.rpc.get_interface_information(interface_name='fe-0/0/7',
           terse=True, normalize=True)
print(etree.tostring(intf_xml,pretty_print=True, encoding='unicode'))

