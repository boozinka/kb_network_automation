#!/usr/bin/env python

# Import libraries
from jnpr_devices import srx2
from jnpr.junos import Device
from jnpr.junos.op.arp import ArpTable
from jnpr.junos.op.routes import RouteTable
from pprint import pprint


# Create an instance of device object
jnpr_dev = Device(**srx2)

# Establish 'netconf' connection
jnpr_dev.open()

my_arps = ArpTable(jnpr_dev)
my_arps.get()

my_routes = RouteTable(jnpr_dev)
my_routes.get()
