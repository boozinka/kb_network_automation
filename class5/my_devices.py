from getpass import getpass

password = getpass()

nxos1 = {'device_type': 'cisco_nxos',
         'host': 'nxos1.lasthop.io',
         'password': password,
         'username': 'pyclass'
}
nxos2 = {'device_type': 'cisco_nxos',
         'host': 'nxos2.lasthop.io',
         'password': password,
         'username': 'pyclass'
}

