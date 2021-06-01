#!/usr/bin/env python

# Import Jinja2 Environment
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

# Set undefined = strict to pick up errors is varibles
env = Environment(undefined=StrictUndefined)
# Set template file location (sub-directory of pwd)
env.loader = FileSystemLoader('./templates')

# Assign varibles
vars_dict = {'ntp_server1': '130.126.24.24',
             'ntp_server2': '152.2.21.1',
             'timezone': 'PST',
             'timezone_offset': '-8',
             'timezone_dst': 'summer-time'
}

template_file = 'ex5_cisco3_config.j2'
# Create template object
template = env.get_template(template_file)
# Render and assign to 'output' varible
output = template.render(**vars_dict)
print(output)

