#!/usr/bin/env python
 
# ConnectHandler
from netmiko import ConnectHandler
from getpass import getpass
from datetime import date, time, datetime

password = 'somepassword'
username = 'fred'

# Create a dictionary of parameters to feed into 'ConnectHandler'
nxos2 = {
    'host': 'nxos2.blah.blah',
    'username': username,
    'password': password,
    'device_type': 'cisco_nxos',
    'global_delay_factor': 2
}

command = 'show lldp neighbors detail'

# Open SSH channel
net_conn = ConnectHandler(**nxos2)

# Add prompt to output and send ping down the channel
output = net_conn.find_prompt()
start_time = datetime.now()
output += net_conn.send_command(command)
end_time = datetime.now()
print('#'*33, ' OUTPUT START ', '#'*33)
print('\n', output, '\n')
print('#'*34, ' OUTPUT END ', '#'*34)
print('\nStart Time = ', start_time)
print('\nEnd Time = ', end_time)
print('\nExecution Time = ', datetime.now() - start_time)

output = net_conn.find_prompt()
start_time = datetime.now()
output += net_conn.send_command(command,delay_factor=8)
end_time = datetime.now()
print('#'*33, ' OUTPUT START ', '#'*33)
print('\n', output, '\n')
print('#'*34, ' OUTPUT END ', '#'*34)
print('\nStart Time = ', start_time)
print('\nEnd Time = ', end_time)
print('\nExecution time = ', datetime.now() - start_time)

net_conn.disconnect


