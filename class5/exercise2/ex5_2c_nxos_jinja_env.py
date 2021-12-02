#!/usr/bin/env python

# Import 'my_devices' module, jinja2, netmiko and misc modules
from my_devices import nxos1, nxos2
from netmiko import ConnectHandler
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from pprint import pprint
import time
import re

# Set undefined = strict to pick up errors is varibles
env = Environment(undefined=StrictUndefined)
# Set template file location (sub-directory of pwd)
env.loader = FileSystemLoader('./templates')


# Assign varibles
nxos1_dict = {'interface': 'Ethernet1/1',
             'ip_addr': '10.1.100.1',
             'netmask': 24,
             'bgp_as': 22
}
nxos2_dict = {'interface': 'Ethernet1/1',
             'ip_addr': '10.1.100.2',
             'netmask': 24,
             'bgp_as': 22
 }

# Update dictionaries with 'peer_ip' addresses
nxos1_dict['peer_ip'] = nxos2_dict['ip_addr']
nxos2_dict['peer_ip'] = nxos1_dict['ip_addr']

# Add the Jinja2 varible dictionaries to the connection dictionaries
nxos1['j2vars'] = nxos1_dict
nxos2['j2vars'] = nxos2_dict

# Loop through each device 
for device in (nxos1, nxos2):
    # Create a copy of the current device connnection dictionary
    tmp_dict = device.copy()
    # Create empty list housing commands rendered and reset on each interation
    cmd_list = []
    # Pop this interations varible dictionary from the list
    j2vars = tmp_dict.pop('j2vars')
    # Split FQDN and assign hostname to a varible for later
    fqdn = device['host'].split('.')
    host = fqdn[0]

    # Render the Jinja2 template to produce commmands
    template_file = 'ex5_2b_nxos_jinja_env.j2'
    template = env.get_template(template_file)
    config = template.render(**j2vars)

    # Convert to a list of commands and strip whitespace
    config_list = config.splitlines()
    for i in config_list:
        cmd_list.append(i.strip())

    # Establish netmiko ssh session
    net_conn = ConnectHandler(**tmp_dict)
    # Save ssh session in dictionary for use later
    device['ssh_conn'] = net_conn
    # Send commands down the channel and print output
    print(f'\nNow configuring {host}...\n')
    cmds = net_conn.send_config_set(cmd_list)
    print(cmds)
    print()

# Give BGP enough time to reach the established state
sleep_time = 15
print(f"Sleeping for {sleep_time} seconds...")
time.sleep(sleep_time)

# Define Pattern for matching BGP status, capture from the end of the string
pattern = re.compile(r'\s+(\S+)\s*$')

# Verify connectivity with ping
for device in (nxos1, nxos2):
    # Retrieve and assign remote ip address to ping
    peer_ip = device['j2vars']['peer_ip']
    ping_cmd = f'ping {peer_ip}'

    # Split FQDN and assign hostname to a varible for later
    fqdn = device['host'].split('.')
    host = fqdn[0]
    
    # Retrieve previous from dictionary and send ping down the channel
    print(f'\nPinging {peer_ip} from {host}...\n')
    net_conn = device['ssh_conn']
    ping_output = net_conn.send_command(ping_cmd)
    print(ping_output)

    # Verify BGP status
    sh_ip_bgp = f'show ip bgp summary | inc {peer_ip}' 
    print(f'\n{sh_ip_bgp}...\n')
    bgp_output = net_conn.send_command(sh_ip_bgp)
    print(bgp_output)

    # Return 'State' value in group(1) and convert to integer
    try:
        bgp_return = re.search(pattern, bgp_output)
        bgp_state = int(bgp_return.group(1))
        # if it converts to integer then state is good and print message
        print(f'\n{host} BGP is established\n')
    # If value returns 'None' integer conversation returns 'Attribute Error'
    except AttributeError:
        print(f'\n{host} BGP is not configured\n')
        break
    # If value returns chars (idle), integer conversation returns 'ValueError'
    except ValueError:
        print(f'\n{host} BGP is not established\n')
        break

# Disconnect both ssh sessions
for device1 in (nxos1, nxos2):
    net_conn1 = device1['ssh_conn']
    net_conn1.disconnect()
