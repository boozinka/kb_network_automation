#!/usr/bin/env python
  
from concurrent.futures import ThreadPoolExecutor, wait
from pprint import pprint
from datetime import date, time, datetime
from my_functions import ssh_command2
from my_devices import cisco3, arista1, arista2, srx2

# Assign varibles
sh_cmd = 'show version'
device_list = [cisco3, arista1, arista2, srx2]

# Record start time
start_time = datetime.now()

# Set the maximum number of threads
max_threads = 4

# Create Thread Pool by creating an instance of the 'TPE' object
pool = ThreadPoolExecutor(max_threads)

futures_list = []
# Loop through each device
for device in device_list:

    # Submit an action to the thread pool and add returned python object
    # to futures list for the 'wait' method
    future = pool.submit(ssh_command2, device, sh_cmd)
    futures_list.append(future)
 
# Waits until all pending threads are complete (list of python objects)
wait(futures_list)

# Iterates through 'futures_list' retrieves device name and prints
# the output of each thread
for future in futures_list:
     # Use result method to extract tuple returned from 'ssh_command2' function
     # and assign it to the 'result' varible
    result = future.result()
    # Extract output and device name from tuple
    output, device_name = result
    print()
    print(device_name, 'output is:')
    print('-'*22, '\n')
    print(output)
    print()

# Record end time
end_time = datetime.now()

# Print the script execution time
print('#'*32, ' EXECUTION TIME ', '#'*32)
print('\nStart Time = ', start_time)
print('\nEnd Time = ', end_time)
print('\nExecution Time = ', datetime.now() - start_time)
print()


