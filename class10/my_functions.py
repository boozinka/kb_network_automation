from netmiko import ConnectHandler
from pprint import pprint

def ssh_command(device_dict, command):
    # Function that establishes netmiko connection and issues a single command
    # and print the output

    # Print header
    print('\nResults for', device_name)
    print('-'*20, '\n')
    
    # Create connection
    net_conn = ConnectHandler(**device_dict)
    
    # Send command down the channel and retrieve output
    output = net_conn.send_command(command)

    # Access FQDN and split to access the device name
    fqdn = device_dict['host'].split('.')
    device_name = fqdn[0]

    # Print results
    pprint(output)
    print()

    # Close connection and return the output
    net_conn.disconnect()
    return output


def ssh_command2(device_dict, command):
    # Function that establishes netmiko connection and issues a single command

    # Access FQDN and split to derive the device name
    fqdn = device_dict['host'].split('.')
    device_name = fqdn[0]

    # Establish a connection with the Context Manager
    with ConnectHandler(**device_dict) as net_conn:
     
        # Return the prompt is not command is submitted
        if command is None:
            return net_conn.find_prompt()
        else:
            # Send command down the channel and retrieve output
            output = net_conn.send_command(command)
            # Return a two element tuple of output and device_name
            return (output, device_name)


def ssh_command3(device_dict, command):
    # Function that establishes netmiko connection and issues a single command

    # Establish a connection with the Context Manager
    with ConnectHandler(**device_dict) as net_conn:

        # Retrieve hostname
        fqdn = net_conn.host.split('.')
        device_name = fqdn[0] 
     
        # Return the prompt is not command is submitted
        if command is None:
            prompt = net_conn_prompt()
            return dict({device_name: prompt})
        else:
            # Send command down the channel and retrieve output
            output = net_conn.send_command(command)
            # Return a two element tuple of output and device_name
            return dict({device_name: output})

