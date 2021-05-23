#!/usr/bin/env python

# ConnectHandler
from netmiko import ConnectHandler
from getpass import getpass

password = 'somepassword'
username = 'fred'

# Create a dictionary of parameters to feed into 'ConnectHandler'
cisco4 = {
    'host': 'cisco4.blah.blah',
    'username': username,
    'password': password,
    'device_type': 'cisco_xe',
}

# Open SSH channel
net_conn = ConnectHandler(**cisco4)

# Add prompt to output and send ping down the channel
output = net_conn.find_prompt()
output += net_conn.send_command_timing('ping', strip_prompt=False, strip_command=False)
output += net_conn.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += net_conn.send_command_timing('8.8.8.8', strip_prompt=False, strip_command=False)
output += net_conn.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += net_conn.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += net_conn.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += net_conn.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += net_conn.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += net_conn.send_command_timing('\n', strip_prompt=False, strip_command=False)

print('\n', output, '\n')

net_conn.disconnect


