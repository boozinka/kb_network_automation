#!/usr/bin/env python

# Import Jinja2 Environment
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

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

# Loop through each dictionary
for var in (nxos1_dict, nxos2_dict):
    template_file = 'ex5_2b_nxos_jinja_env.j2'
    # Create template object
    template = env.get_template(template_file)
    # Render and assign to 'output' varible
    output = template.render(**var)
    print(output)

