#!/usr/bin/env python

""" Program with simple function to illustrate pytest and fixtures """
 
# ConnectHandler
import pytest
from netmiko import ConnectHandler

# Decorator registering the following function as a fixture and setting scope
@pytest.fixture(scope='module')
def netmiko_object(request):
    """ Connect to device and and return the connection object """

    # Receive the incoming parameter
    device = request.param

    # Establish SSH connection and assign object to 'net_conn'
    net_conn = ConnectHandler(**device)

    # 'fin' tears down the SSH connection
    def fin():
        net_conn.disconnect()

    # 'addfinalizer' calls 'fin' when test are complete
    request.addfinalizer(fin)

    # Return connection object
    return net_conn 

