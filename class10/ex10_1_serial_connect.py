#!/usr/bin/env python
  
from netmiko import ConnectHandler
from pprint import pprint
from datetime import date, time, datetime
from my_devices import cisco3, arista1, arista2, srx2

# Assigh varibles
sh_cmd = 'show version'
device_list = [cisco3, arista1, arista2, srx2]

def netmiko_connect(device_dict, command):
    # Function that establishes netmiko connection and issues a single command

    net_conn = ConnectHandler(**device_dict)
    output = net_conn.send_command(command)
    net_conn.disconnect()
    return output

# Record start time
start_time = datetime.now()

# Loop through each device, establish connection, run 'sh ver' and print output
for device in device_list:
    output = netmiko_connect(device, sh_cmd)
    fqdn = device['host'].split('.')
    device_name = fqdn[0]
    print('\nResults for', device_name)
    print('-'*20, '\n')
    pprint(output)
    print()

# Record end time
end_time = datetime.now()

# Print the script execution time
print('#'*32, ' EXECUTION TIME ', '#'*32)
print('\nStart Time = ', start_time)
print('\nEnd Time = ', end_time)
print('\nExecution Time = ', datetime.now() - start_time)
print()


