#!/usr/bin/env python

# Import libraries
from jnpr_devices import srx2
from jnpr.junos import Device
from jnpr.junos.exception import LockError
from jnpr.junos.utils.config import Config
from jnpr.junos.op.routes import RouteTable
from ex8_2_pyez_tables_views import check_connected, gather_routes
from pprint import pprint
import ipdb


def open_device(device):
    #Function to lock the device or exit gracefully

    # Create a configuration object/varible using a configuration class
    # and acquire configuration lock
    cfg = Config(device)
    try:
        cfg.lock()
    except LockError:
        print('\nThis device is already in use and locked by another user\n')
    return cfg


def config_device(cfg, conf_file, commit_msg):
    # Retrieve the routing table before and after your configuration change
    # and print out the differences 

    # Use the "load" plus 'conf' method to stage a configuration from a file
    cfg.load(path=conf_file, format='text', merge=True)

    # Commit the changes and add a comment to the commit
    if cfg.diff():
        cfg.commit()
        cfg.commit(comment= commit_msg)
    cfg.unlock()


def compare_config(initial_routes, updated_routes):
    # Takes two configs and print the difference 

    # Initilise varibles
    diff_list = []

    # Create new list with only the differences in it
    for route in updated_routes.keys():
        if route not in initial_routes.keys():
            diff_list.append(route)

    # Print the before commit config (initial_routes)
    print('\nThe before commit configuration was.')
    print('-'*40, '\n')
    for route in initial_routes.keys():
        print(route)
    print()

    # Print the after commit config (updated_routes)
    print('\nThe after commit configuration is.')
    print('-'*40, '\n')
    for route in updated_routes.keys():
        print(route)
    print()

    # Print the difference between the two configurations
    print('\nThe follow routes have been added to the configuration.')
    print('-'*45, '\n')
    for route in diff_list:
        print(route)
    print()


def remove_routes(cfg, commit_msg):
    # Function to remove static routes using the load plus 'set' method

    cfg.load("delete routing-options static route 203.0.113.11/32",
              format="set", merge=True)
    cfg.load("delete routing-options static route 203.0.113.101/32",
              format="set", merge=True)

    # Commit the changes and add a comment to the commit
    if cfg.diff():
        cfg.commit()
        cfg.commit(comment= commit_msg)
    cfg.unlock()

# Exercise 4a
# Using "jnpr_devices.py" connect to srx2 and gather the current routing table

# Create an instance of device object
jnpr_dev = Device(**srx2)

# Establish 'netconf' connection
jnpr_dev.open()

# Call function to check established connection
conn = check_connected(jnpr_dev)

# Call funtions to retrieve the routing and arp tables
initial_routes = gather_routes(jnpr_dev)

# Exercise 4b
# Assign varible and call configure function to create new static routes
conf_file = 'static_routes.conf'
commit_msg = 'WB Exercise8.4c adding static routes'

# Call function to create configuration instance 
cfg = open_device(jnpr_dev)

# Call function to configure end device
config_device(cfg, conf_file, commit_msg)

# Exercise 4c
# Retrieve updated routing table and run a diff against the previous one

updated_routes = gather_routes(jnpr_dev)
compare_config(initial_routes, updated_routes)

# Exercise 4d
# Delete the static routes configured in Exercise 4c

# Assign varible and call configure function to create new static routes
commit_msg = 'WB Exercise8.4d deleting static routes'

# Call function to create configuration instance 
cfg = open_device(jnpr_dev)

# Call function to delete the static routes configured in Exercise 4c
remove_routes(cfg, commit_msg)
  
