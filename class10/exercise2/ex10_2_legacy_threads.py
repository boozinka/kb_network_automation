#!/usr/bin/env python
  
import threading
from pprint import pprint
from datetime import date, time, datetime
from my_functions import ssh_command
from my_devices import cisco3, arista1, arista2, srx2

# Assign varibles
sh_cmd = 'show version'
device_list = [cisco3, arista1, arista2, srx2]

# Record start time
start_time = datetime.now()

# Loop through each device
for device in device_list:
    
    # Use threading library to start new thread, passing a reference to the
    # 'ssh_command' function and it's arguments
    my_thread = threading.Thread(target=ssh_command, args=(device, sh_cmd))

    # Start the thread
    my_thread.start()

# Main thread reference
main_thread = threading.currentThread()

# Loop through all outstanding threads until they are all complete
# The main thread is running the 'for loop', so avoiding it, avoids
# getting into an infinite loop
for some_thread in threading.enumerate():
    if some_thread != main_thread:
        print(some_thread)
        # Join waits until 'some_thread' is complete
        some_thread.join()

# Record end time
end_time = datetime.now()

# Print the script execution time
print('#'*32, ' EXECUTION TIME ', '#'*32)
print('\nStart Time = ', start_time)
print('\nEnd Time = ', end_time)
print('\nExecution Time = ', datetime.now() - start_time)
print()


