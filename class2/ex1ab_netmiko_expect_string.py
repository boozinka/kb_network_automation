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

# Create a dictionary for extended Ping commands and additional prompts
ext_ping = {
    'command': ('ping', r'Protocol'),
    'Protocol [ip]' : ('\n', r'Target'),
    'Target IP address' : ('8.8.8.8', r'Repeat count'),
    'Repeat count' : ('\n', r'Datagram'),
    'Datagram size' : ('\n', r'Timeout'),
    'Timeout in seconds' : ('\n', r'Extended'),
    'Extended commands' : ('\n', r'Sweep'),
    'Final CR' : ('\n', r'#')
}

# Establish SSH tunnel
net_conn = ConnectHandler(**cisco4)

# Find and print prompt
prompt = net_conn.find_prompt()
output = prompt

"""
Send commands down the tunnel for Ping and include each expect string (prompt)
'stip_prompt' and 'strip_command' = False to display full output
"""
for keys,values in ext_ping.items():
    output += net_conn.send_command(values[0], expect_string=values[1],
                                    strip_prompt=False, strip_command=False)

print('\n', output, '\n')

net_conn.disconnect

