#!/usr/bin/env python
  
from concurrent.futures import ProcessPoolExecutor, as_completed
from pprint import pprint
from datetime import date, time, datetime
from my_functions import ssh_command3
from my_devices import cisco3, arista1, arista2, srx2

# Assign varibles
cmd_list = [] 
device_list = [cisco3, arista1, arista2, srx2]

# Record start time
start_time = datetime.now()

# Set the maximum number of threads/processes
max_threads = 4

# Use Context Manager when creating a process pool
with ProcessPoolExecutor(max_threads) as pool:

    # Iterate over device_list identifying device type, then add the
    # relevant command to the cmd_list for use in the results_generator
    for device in device_list:
        if 'junos' in device['device_type']:
            cmd_list.append('show arp')
        else:
            cmd_list.append('show ip arp')

    # Submit an action to the process pool using the '.map' method
    # Map passes an item from iterable (device_list) and iterable (cmd_list)
    # into 'ssh_commmand3' and returns a python iterable object (list)
    results_generator = pool.map(ssh_command3, device_list, cmd_list) 

    # Iterates through 'results_generator' list of dictionaries and prints
    # a header with the device name and the output as each process completes.
    for result in results_generator:
        for device_name, output in result.items():
            print('\n\n')
            print(device_name.capitalize(), 'Output:')
            print('-'*25, '\n')
            print(output)
            print()

# Record end time, and print the execution time
print('\nExecution Time = ', datetime.now() - start_time)





