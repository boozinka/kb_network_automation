#!/usr/bin/env python

# SSH Connect Using Netmiko
#
# Makes an SSH connection using Netmiko

# ConnectHandler
from netmiko import Netmiko
from getpass import getpass
from pprint import pprint
from datetime import date, time, datetime

# Create dicionary of parameter to feed into 'net_connect'
cisco3 = {
    'host': 'cisco3.blah.blah',
    'username': 'fred',
    'password': 'somepassword',
    'device_type': 'cisco_ios',
    'fast_cli': True
}

# Assign varibles
sh_dns_view = 'show ip dns view'
ping_google = 'ping google.com'

# Assign tuple containing unset configuration commands
unset_cmds = ('no ip name-server 1.1.1.1',
              'no ip name-server 1.0.0.1',
              'no ip domain-lookup'
)

# Assign tuple containing set configuration commands
set_cmds = ('ip name-server 1.1.1.1',
            'ip name-server 1.0.0.1',
            'ip domain-lookup'
)

# Establish SSH Connection
net_conn = Netmiko(**cisco3)

# Send command down the channel to list before settings
print('#'*33, ' SETTINGS BEFORE CONFIG ', '#'*33)
print()
sh_dns = net_conn.send_command(sh_dns_view)
pprint(sh_dns)

# Record start time
start_time = datetime.now()

# Send commands down the channel in a for loop to configure device
for i in set_cmds:
    net_conn.send_config_set(i)

# Record end time
end_time = datetime.now()

# Send command down the channel to list before settings
print('#'*33, ' SETTINGS AFTER CONFIG ', '#'*33)
print()
sh_dns = net_conn.send_command(sh_dns_view)
ping_cmd = net_conn.send_command(ping_google, strip_prompt=False, strip_command=False)
pprint(sh_dns)
pprint(ping_cmd)

# Print the script execution time
print('#'*32, ' EXECUTION TIME ', '#'*32)
print('\nStart Time = ', start_time)
print('\nEnd Time = ', end_time)
print('\nExecution Time = ', datetime.now() - start_time)

net_conn.disconnect()
