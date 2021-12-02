#!/usr/bin/env python

from getpass import getpass

password = getpass()

cisco3 = {
   'host': 'cisco3.lasthop.io',
   'device_type': 'cisco_ios',
   'username': 'pyclass',
   'password': password
}
arista1 = {
   'host': 'arista1.lasthop.io',
   'device_type': 'arista_eos',
   'username': 'pyclass',
   'password': password,
   'global_delay_factor': 4
}
arista2 = {
   'host': 'arista2.lasthop.io',
   'device_type': 'arista_eos',
   'username': 'pyclass',
   'password': password,
   'global_delay_factor': 4
}
srx2 = {
   'host': 'srx2.lasthop.io',
   'device_type': 'juniper_junos',
   'username': 'pyclass',
   'password': password
}

