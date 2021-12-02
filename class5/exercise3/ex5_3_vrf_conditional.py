#!/usr/bin/env python

# Import Jinja2 Environment
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

# Set undefined = strict to pick up errors is varibles
env = Environment(undefined=StrictUndefined)
# Set template file location (sub-directory of pwd)
env.loader = FileSystemLoader('./templates')

# Assign varibles
vars_dict = {'vrf_name': 'blue',
             'rd_num': '100:1',
             'ipv4_enable': True,
             'ipv6_enable': True
}

template_file = 'ex5_3_vrf_conditional.j2'
# Create template object
template = env.get_template(template_file)
# Render and assign to 'output' varible
output = template.render(**vars_dict)
print(output)

