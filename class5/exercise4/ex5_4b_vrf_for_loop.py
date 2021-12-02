#!/usr/bin/env python

# Import Jinja2 Environment
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

# Set undefined = strict to pick up errors is varibles
env = Environment(undefined=StrictUndefined)
# Set template file location (sub-directory of pwd)
env.loader = FileSystemLoader('./templates')

# Assign varibles
blue_vrf = {'vrf_name': 'blue',
            'rd_num': '100:1',
            'ipv4_enable': True,
            'ipv6_enable': True
}
red_vrf = {'vrf_name': 'red',
           'rd_num': '200:1',
           'ipv4_enable': True,
           'ipv6_enable': True
}
green_vrf = {'vrf_name': 'green',
             'rd_num': '300:1',
             'ipv4_enable': True,
             'ipv6_enable': True
}
yellow_vrf = {'vrf_name': 'yellow',
              'rd_num': '400:1',
              'ipv4_enable': True,
              'ipv6_enable': True
}
orange_vrf = {'vrf_name': 'orange',
              'rd_num': '500:1',
              'ipv4_enable': False,
              'ipv6_enable': True
}

# Add VRF dictionaries to a list to iterate over
vrf_list = [blue_vrf, red_vrf, green_vrf, yellow_vrf, orange_vrf]

# Add 'vrf_list' to a dictionary to be rendered
vrf_dict = {'vrf_list': vrf_list}

# Specify template file
template_file = 'ex5_4_vrf_for_loop.j2'

# Create template object
template = env.get_template(template_file)
# Render and assign to 'output' varible
output = template.render(**vrf_dict)
print(output)

