#!/usr/bin/env python
  
from concurrent.futures import ProcessPoolExecutor, as_completed
from pprint import pprint
from datetime import date, time, datetime
from my_functions import ssh_command3
from my_devices import cisco3, arista1, arista2, srx2

# Assign varibles
sh_cmd = 'show version'
device_list = [cisco3, arista1, arista2, srx2]

# Record start time
start_time = datetime.now()

# Set the maximum number of threads/processes
max_threads = 4

# Create Process Pool by creating an instance of the 'PPE' object
pool = ProcessPoolExecutor(max_threads)

# Create a list to append process to
futures_list = []

# Loop through each device
for device in device_list:
 
    # Submit an action to the process pool and add returned python object
    # to futures list for the 'wait' method
    future = pool.submit(ssh_command3, device, sh_cmd)
    futures_list.append(future)
 
# Iterates through 'futures_list' of dictionaries and prints a header
# with the device name and the output as each process completes.
for future in as_completed(futures_list):

     # Use result method to extract dictionary returned from 'ssh_command3' function
     # and assign it to the 'result' varible
    result = future.result()

     # Iterate through the dictionary and extract device name and output
    for device_name, output in result.items():
        print('\n\n')
        print(device_name, 'Output is:')
        print('-'*25, '\n')
        print(output)
        print()

# Record end time, and print the execution time
print('\nExecution Time = ', datetime.now() - start_time)





