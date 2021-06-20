#!/usr/bin/env python

# Import libraries
import logging
from jnpr_devices import srx2
from jnpr.junos import Device
from jnpr.junos.exception import LockError
from jnpr.junos.utils.config import Config
from pprint import pprint

def log_traceback(ex):
    tb_lines = traceback.format_exception(ex.__class__, ex, ex.__traceback__)
    tb_text = ''.join(tb_lines)
    # I'll let you implement the ExceptionLogger class and the timestamping.
    exception_logger.log(tb_text)

# Create an instance of device object
jnpr_dev = Device(**srx2)

# Establish 'netconf' connection
jnpr_dev.open()

# Set timeout to 60 seconds, used for cmds that take a long time
jnpr_dev.timeout = 60

# Exercise 3a
# Obtain a configuration lock
cfg = Config(jnpr_dev)
cfg.lock()

# Try to acquire a configuration lock again
print('\nExercise 3a, try to acquire a second configuration lock\n')
try:
    cfg.lock()
except LockError:
    print('\nThis device is already in use and locked by another user\n')


# Exercise 3b
# Use the "load" method to stage a configuration using a basic set command
print('\nExercise 3b, use "load" method to stage a configration\n')
cfg.load('set system host-name python4life', format='set', merge=True)


# Exercise 3c
# Print the diff of the current configuration with the staged configuration
print('\nExercise 3c, print the "diff" of the current and staged config\n')
print(cfg.diff())
print()


# Exercise 3d
# Rollback the staged configuration and print out the diff  
print('\nExercise 3d, rollback the staged configuration and print "diff"\n')
cfg.rollback()
print(cfg.diff())
print()
cfg.unlock()

