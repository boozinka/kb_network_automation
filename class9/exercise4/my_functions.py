from napalm import get_network_driver

### Using the Context Manager ###

# >>> from napalm import get_network_driver
# >>> driver = get_network_driver('eos')
# >>> with driver('localhost', 'vagrant', 'vagrant', optional_args={'port': 12443}) as device:
# ...     print(device.get_facts())
# ...     print(device.get_interfaces_counters())


# Open the napalm connection to the device and return the napalm connection object.
def napalm_conn(device):
    # Function open a napalm connection and return the connection object

    # Copy device to avoid modifying original copy and future 'pop' errors
    device = device.copy()
    # pop device type, as this is an invalid kwarg for napalm
    device_type = device.pop('device_type')
    # Identify underlying driver by passing the 'device_type'
    driver = get_network_driver(device_type)
    # Pass device to NAPALM with driver
    conn = driver(**device)
    # Open connection object
    conn.open()
    # Return connection object
    return conn 


def backup_config(device):
    # This function accepts a connection object retrieve the config
    # and backs up the running config by writing it to a file

    # Acquire the config of each device and assign to 'config'
    config = device.get_config()['running']

    # Acquire device objects fqdn and use the host portion to form filename
    fqdn = device.hostname.split('.')
    filename = str(fqdn[0]) + '_config.txt'

    # Write the config to a file
    with open(filename, 'w') as f:
        f.write(config)

def create_checkpoint(device):
    # Function to retrieve a checkpoint from NXOS device and write it to a file

    # Retrieve checkpoint from NXOS device
    checkpoint = device._get_checkpoint_file()

    # Write the checkpoint to a file
    with open('nxos1.checkpoint', 'w') as f:
       print(checkpoint, file=f)

 
    
