#!/usr/bin/env python

# Import libraries
from jnpr_devices import srx2
from jnpr.junos import Device
from jnpr.junos.op.arp import ArpTable
from jnpr.junos.op.routes import RouteTable
from pprint import pprint
import sys


def check_connected(device):
    # Function to confirm an established connection
    if device.connected:
        print(f"\nConnection to {device.hostname} established\n")
    else:
        print("\nConnection to {device.hostname} not established\n")
        sys.exit(1)

def gather_routes(device):
    # Funtion to retrieve the routing table
    my_routes = RouteTable(device)
    my_routes.get()
    return my_routes


def gather_arp_table(device):
    # Funtion to retrieve the arp table
    my_arps = ArpTable(device)
    my_arps.get()
    return my_arps


def print_output(device, my_routes, my_arps):
    # Function to print out the 'hostname', NETCONF port, username,
    # routing table and arp table

    # Print the device hostname, username and NETCONF port
    print(f"\nThe device hostname is {device.hostname}\n")
    print(f"The user connected is {device.user}\n")
    print(f"The NETCONF port is {device.port}\n")

    # Prints the header for the routing table
    print(f"\n{'Protocol': <10}{'Prefix': >20}{' ': ^5}{'via': <10}"
          f"{'Next Hop': >20}")
    print('-'*80, '\n')

    # Iterates through the structure and prints out the routing table
    for prefix in my_routes.keys():
        prefix_attr = my_routes[prefix]
        proto = prefix_attr['protocol']
        via = prefix_attr['via']
        age = prefix_attr['age']
        nhop = prefix_attr['nexthop']
        print(f"{proto: <10}{prefix: >20}{' ': ^5}{via: <10}{str(nhop): >20}")
    print()

    # Prints the header for the arp table
    print(f"\n{'Mac Address': <20}{'IP Address': >20}{' ': ^5}{'Interface':<20}")
    print('-'*60, '\n')

    # Iterates through the structure and prints out the arp table
    for arp_entry in my_arps.keys():
        arp_attr = my_arps[arp_entry]
        mac = arp_attr['mac_address']
        ip_addr = arp_attr['ip_address']
        intf = arp_attr['interface_name']
        print(f"{mac: <20}{ip_addr: >20}{' ': ^5}{intf:<20}")
    print()


def main():
    # Function that acts as the main program

    # Create an instance of device object
    jnpr_dev = Device(**srx2)

    # Establish 'netconf' connection
    jnpr_dev.open()

    # Call function to check established connection
    conn = check_connected(jnpr_dev)

    # Call funtions to retrieve the routing and arp tables
    my_routes = gather_routes(jnpr_dev)
    my_arps = gather_arp_table(jnpr_dev)

    # Call function to print out the desired output attributes
    print_output(jnpr_dev, my_routes, my_arps)


if __name__ == "__main__":


    main()
 
