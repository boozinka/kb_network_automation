#!/usr/bin/env python

# SSH Connect Using Netmiko
#
# Makes an SSH connection using Netmiko

# ConnectHandler
from netmiko import Netmiko
from getpass import getpass
from pprint import pprint
from datetime import date, time, datetime
import time

# Ask for enable secret password
password = getpass()

# Create dicionary of parameter to feed into 'net_connect'
cisco4 = {
    'host': 'cisco4.blah.blah',
    'username': 'fred',
    'password': 'somepassword',
    'secret': password,
    'device_type': 'cisco_ios',
    'session_log': 'ex6_output.txt'
}

# Establish SSH Connection
net_conn = Netmiko(**cisco4)

# Find and print the prompt
prompt = net_conn.find_prompt()
print('\nCurrent prompt = {}'.format(prompt))

# Enter 'config_mode()', print the prompt and exit
net_conn.config_mode()
prompt = net_conn.find_prompt()
print('\nThe prompt is now = {}'.format(prompt))
net_conn.exit_config_mode()

"""
When using 'write_channel()' you need to terminate the command with '\n'
When using 'read_channel()' to read the output back you need to add a 
sleeper timer.
"""

# Use 'write_channel()' method to send disable down the channel
net_conn.write_channel('disable\n')
time.sleep(2)
output = net_conn.read_channel()
print('\nWrite channel output is {}'.format(output))

# Execute the 'enable()' method and print the current prompt
net_conn.enable()
prompt = net_conn.find_prompt()
print('\nThe prompt is now = {}'.format(prompt))

net_conn.disconnect()
