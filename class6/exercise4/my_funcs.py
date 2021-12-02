import yaml
from pprint import pprint

def yaml_import(file):
    # imports a yaml file and returns a data structure

    with open(file) as f:
        data_struc = yaml.load(f)

    return data_struc


def arp_out(arp_list):
    # Iterates through a list of dictionaries and
    # prints out the IP to MAC Address mappings

    # Loops over each devie entry in the list
    for device_dict in arp_list:
        # Loops over each devices dictionary key value pairs
        for device_name, device_arp_list in device_dict.items():
            # Prints the device name and header for the mappings
            print()
            print(f'Device mapping for {device_name}')
            print()
            print(f"{'IP Address': >17}{'     ': ^5}{'MAC Address': >16}")
            print('-'*40)
            print()
            # Loops over each arp entry in the list, extracts and prints
            for arp_dict in device_arp_list:
                ip_addr = arp_dict['address']
                mac_addr = arp_dict['hwAddress']
                print(f"{ip_addr: >17}{' --> ': ^5}{mac_addr: >16}")
            print()
        print()
 
