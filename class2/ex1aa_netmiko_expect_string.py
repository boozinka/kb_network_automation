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

# set command varibles
command = 'ping'
target_ip = '8.8.8.8'

# Establish SSH tunnel
net_conn = ConnectHandler(**cisco4)

# Find and print prompt
prompt = net_conn.find_prompt()
output = prompt

# Send commands down the tunnel for Ping and included each expect string (prompt)
# 'stip_prompt' and 'strip_command' = False to display full output

output += net_conn.send_command(command, expect_string=r'Protocol', strip_prompt=False,
                                strip_command=False)
output += net_conn.send_command('\n', expect_string=r'Target', strip_prompt=False,
                                strip_command=False)
output += net_conn.send_command(target_ip, expect_string=r'Repeat count', strip_prompt=False,
                                strip_command=False)
output += net_conn.send_command('\n', expect_string=r'Datagram', strip_prompt=False,
                                strip_command=False)
output += net_conn.send_command('\n', expect_string=r'Timeout', strip_prompt=False,
                                strip_command=False)
output += net_conn.send_command('\n', expect_string=r'Extended', strip_prompt=False,
                                strip_command=False)
output += net_conn.send_command('\n', expect_string=r'Sweep', strip_prompt=False,
                                strip_command=False)
output += net_conn.send_command('\n', expect_string=r'#', strip_prompt=False,
                                strip_command=False)
print('\n', output, '\n')

net_conn.disconnect

