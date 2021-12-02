#!/usr/bin/env python

""" Program with simple function to illustrate pytest and fixtures """
 
# ConnectHandler
import pytest
from netmiko import ConnectHandler
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

# Decorator registering the following function as a fixture and setting scope
@pytest.fixture(scope='module')
def netmiko_object(request):
    """ Connect to device and and return the connection object """

    # Receive the incoming parameter
    device = request.param

    return ConnectHandler(**device)

# Decorator parametrizing 'netmiko_object' with devices from 'device_list'
@pytest.mark.parametrize('netmiko_object', device_list, indirect=True)
def test_netmiko_prompt(netmiko_object):
    """ Function to test 'netmiko_object' function """

    assert netmiko_object.find_prompt() == 'arista1#'


@pytest.mark.parametrize('netmiko_object', device_list, indirect=True)
def test_netmiko_sh_ver(netmiko_object):
    """ Function to test 'netmiko_object' function """

    assert '4.20.10M' in netmiko_object.send_command('show version')

