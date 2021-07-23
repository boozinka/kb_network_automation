#!/usr/bin/env python

""" Program with simple function to illustrate pytest and fixtures """
 
# ConnectHandler
from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

# Create a dictionary of parameters to feed into 'ConnectHandler'
arista1 = {
    'host': 'arista1.lasthop.io',
    'username': 'pyclass',
    'password': password,
    'device_type': 'arista_eos',
}


def netmiko_object(device):
    """ Connect to device and and return the connection object """

    net_conn = ConnectHandler(**device)
    return net_conn


def test_netmiko_prompt():
    """ Function to test 'netmiko_object' function """

    result = netmiko_object(arista1)
    assert result.find_prompt() == 'arista1#'


def test_netmiko_sh_ver():
    """ Function to test 'netmiko_object' function """

    result = netmiko_object(arista1)
    assert '4.20.10M' in result.send_command('show version')

