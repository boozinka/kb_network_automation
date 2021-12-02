#!/usr/bin/env python

""" Test functions using fixture from 'conftest.py' """

# ConnectHandler
import pytest
from getpass import getpass

# Retrieve password
password = getpass()

# Create a dictionary of parameters to feed into 'ConnectHandler'
arista1 = {
    'host': 'arista1.lasthop.io',
    'username': 'pyclass',
    'password': password,
    'device_type': 'arista_eos',
}

# Create device_list
device_list = [arista1]

# Decorator parametrizing 'netmiko_object' with devices from 'device_list'
@pytest.mark.parametrize('netmiko_object', device_list, indirect=True)
def test_netmiko_prompt(netmiko_object):
    """ Function to test 'netmiko_object' function """

    assert netmiko_object.find_prompt() == 'arista1#'


@pytest.mark.parametrize('netmiko_object', device_list, indirect=True)
def test_netmiko_sh_ver(netmiko_object):
    """ Function to test 'netmiko_object' function """

    assert '4.20.10M' in netmiko_object.send_command('show version')
