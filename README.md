# kb_network_automation
Following Kirk Byers Python Network Automation Course

This course dives into Python as applied to Network Engineering.

### Topics covered include:

- [ ] Git
- [ ] Netmiko
- [ ] Complex Data Structures
- [ ] YAML/JSON
- [ ] CiscoConfParse
- [ ] Python Libraries
- [ ] TextFSM
- [ ] Jinja2
- [ ] Arista eAPI
- [ ] XML
- [ ] NX-OS NX-API
- [ ] NETCONF
- [ ] Juniper PyEZ
- [ ] NAPALM
- [ ] SSH and Concurrency
- [ ] *Using a REST API (Plus and Premium Packages Only)
- [ ] *pytest, tox, and Travis CI (Premium Package Only)
- [ ] Create commit conflicts in the local repository
- [ ] Play aroung with modifying files and commit conflicts



Class 1.

- [ ] I.    Why care about Git?               
- [ ] II.   Git - Getting Started              
- [ ] III.  Git - Adding and Removing Files              
- [ ] IV.   Git - Push and Pull            
- [ ] V.    Git - Branches           
- [ ] VI.   Git - Rebase           
- [ ] VII.  Git - Common Workflow           
- [ ] VIII. Netmiko Overview          
- [ ] IX.   Netmiko send_command()        


GIT
1. Create a GitHub account (it's free for public repositories).

2. Create a new repository in GitHub for this class. Add a README file and a Python .gitignore file.

3. Clone the repository that you just created on GitHub into your home directory in the lab environment.

4. Configure your name and email address on the lab server: 

$ git config --global user.name "John Doe"
$ git config --global user.email jdoe@domain.com

5. Add and commit three files into your repository in the lab environment. Use 'git status' to verify that all your changes have been committed and that you are working on the 'main' branch.  Push these changes up to GitHub.

6. Create a 'test' branch in your repository.
    a. Ensure that you are working on the 'test' branch.
    b. Add two directories to the 'test' branch. Each directory should contain at least one file. These files should be committed into the 'test' branch.
    c. Use 'git log' to look at your history of commits.
    d. Modify one of your previously committed files. Use 'git diff' to look at the pending changes in this file. Add and commit these changes.

7. Push the 'test' branch up to GitHub.

8. Create a Pull Request inside of GitHub (pull request that would merge the 'test' branch into the 'main' branch). Look at the 'files changed' in the pull request. Merge the pull request.

9. Back on your AWS server
    a. Switch back to the 'main' branch.
    b. Use a 'git pull' to retrieve all of the updates from GitHub on the main branch.
    c. Verify your 'main' branch now has all of the changes that you had previously made in the 'test' branch.

10. In the 'main' branch use 'git rm' to remove some file from the branch. Commit this change.

11. Edit one of your files. Once again use 'git diff' to look at the change pending in that file. Use 'git checkout -- <file>' to discard that pending change. Verify your 'git status' is now clean.

12. In GitHub, edit the README.md file and commit a change to the 'main' branch in GitHub. On the lab server also edit the README.md file and commit the change into the lab server. Use 'git pull' to pull the 'main' branch from GitHub into the lab server. At this point you should have a merge conflict. It should look something like this: 

$ git pull origin main
From https://github.com/ktbyers/pyneta
 * branch            main     -> FETCH_HEAD
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.

Edit the README.md file to correct the merge conflict. The README.md file should have something like the following inside of it:

$ cat README.md 
# pyneta
Test PyNet Repository

Some additional information on this repository.

<<<<<<< HEAD
Create a merge conflict.
=======
More changes to readme.
>>>>>>> 1690ce5a6ddb640198ccf3bca26f32a65d772b92

The '<<<<<', '=====', '>>>>>' indicate where the inconsistencies on the file are. Git is basically stating I have this first line(s) from one change and this second line(s) from another change and I don't know which one you want to keep. Which line do you want to keep (could be one of the lines, both of the lines, none of the lines).

Here is how I fixed the merge conflict in the above file: 

$ cat README.md 
-----------------
# pyneta
Test PyNet Repository

Some additional information on this repository.

Create a merge conflict.

More changes to readme.
-----------------

# Then I need to add and commit the file
$ git add README.md 
$ git commit -m "Fixing merge conflict"
[main e87901a] Fixing merge conflict


Netmiko

1. In the lab environment use Netmiko to connect to one of the Cisco NX-OS devices. You can find the IP addresses and username/passwords of the Cisco devices in the 'Lab Environment' email or alternatively in the ~/.netmiko.yml file. Simply print the router prompt back from this device to verify you are connecting to the device properly.

2. Add a second NX-OS device to your first exercise. Make sure you are using dictionaries to represent the two NX-OS devices. Additionally, use a for-loop to accomplish the Netmiko connection creation. Once again print the prompt back from the devices that you connected to.

3. For one of the Cisco IOS devices, use Netmiko and the send_command() method to retrieve 'show version'. Save this output to a file in the current working directory.



Class 2.

- [ ] I.    Netmiko Handling Additional Prompts
- [ ] II.   Netmiko Delay Factor              
- [ ] III.  Netmiko and TextFSM              
- [ ] IV.   Netmiko and Config Changes            
- [ ] V.    Netmiko and Secure Copy           
- [ ] VI.   Netmiko save_config(), keys, and fast_cli      
- [ ] VII.  Netmiko Misc Topics  


1. Use the extended 'ping' command and Netmiko on the 'cisco4' router. This should prompt you for additional information as follows:

cisco4#ping
Protocol [ip]: 
Target IP address: 8.8.8.8
Repeat count [5]: 
Datagram size [100]: 
Timeout in seconds [2]: 
Extended commands [n]: 
Sweep range of sizes [n]: 
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/4 ms

a. Use send_command_timing() to handle the additional prompting from this 'ping' command. Specify a target IP address of '8.8.8.8'

b. Use send_command() and the expect_string argument to handle the additional prompting. Once again specify a target IP address of '8.8.8.8'.


2. Create a Netmiko connection to the 'nxos2' device using a global_delay_factor of 2. Execute 'show lldp neighbors detail' and print the returned output to standard output. Execute 'show lldp neighbors detail' a second time using send_command() with a delay_factor of 8. Print the output of this command to standard output. Use the Python datetime library to record the execution time of both of these commands. Print these execution times to standard output.


3. On your AWS lab server, look at the ntc-templates index file (at ~/ntc-templates/templates/index). Look at some of the commands available for cisco_ios (you can use 'cat ~/ntc-templates/templates/index | grep cisco_ios' to see this). Also look at some of the abbreviated forms of Cisco IOS commands that are supported in the index file.

Create a script using Netmiko that executes 'show version' and 'show lldp neighbors' against the Cisco4 device with use_textfsm=True.

What is the outermost data structure that is returned from 'show lldp neighbors' (dictionary, list, string, something else)? The Cisco4 device should only have one LLDP entry (the HPE switch that this router connects to). From this LLDP data, print out the remote device's interface. In other words, print out the port number on the HPE switch that Cisco4 connects into.


4. Use Netmiko and the send_config_set() method to configure the following on the Cisco3 router.

ip name-server 1.1.1.1
ip name-server 1.0.0.1
ip domain-lookup

Experiment with fast_cli=True to see how long the script takes to execute (with and without this option enabled).

Verify DNS lookups on the router are now working by executing 'ping google.com'. Verify from this that you receive a ping response back.


5. On both the NXOS1 and NXOS2 switches configure five VLANs including VLAN names (just pick 5 VLAN numbers between 100 - 999). Use Netmiko's send_config_from_file() method to accomplish this. Also use Netmiko's save_config() method to save the changes to the startup-config.


6. Using SSH and netmiko connect to the Cisco4 router. In your device definition, specify both an 'secret' and a 'session_log'. Your device definition should look as follows: 

password = getpass()
device = {
    "host": "cisco4.blah.net",
    "username": "fred",
    "password": somepassword,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}

Execute the following sequence of events using Netmiko:

a. Print the current prompt using find_prompt()

b. Execute the config_mode() method and print the new prompt using find_prompt()

c. Execute the exit_config_mode() method and print the new prompt using find_prompt()

d. Use the write_channel() method to send the 'disable' command down the SSH channel. Note, write_channel is a low level method so it requires that you add a newline to the end of your 'disable' command.

e. time.sleep for two seconds and then use the read_channel() method to read the data that is currently available on the SSH channel. Print this to the screen.

f. Execute the enable() method and print your now current prompt using find_prompt(). The enable() method will use the 'secret' defined in your device definition. This 'secret' is the same as the standard lab password.

g. After you are done executing your script, look at the 'my_output.txt' file to see what is included in the session_log.


Notes: both the send_config_set() and send_config_from_file() methods automatically enter and exit config mode; consequently, you don't typically need to control this yourself. The write_channel() and read_channel() methods can be useful if you need to make a custom solution to write/read the SSH channel in some way. The session_log can be very helpful for debugging Netmiko issues to see what occurred during the SSH session.


Class 3.

- [ ] I.    Handling Complex Data Structures
- [ ] II.   Changing Data Structure Format             
- [ ] III.  Serialization Protocols
- [ ] IV.   YAML           
- [ ] V.    JSON          
- [ ] VI.   CiscoConfParse  (Part1)      
- [ ] VII.  CiscoConfParse  (Part2)          
- [ ] VIII. CiscoConfParse  (Part3)    


1. Using the below ARP data, create a five element list. Each list element should be a dictionary with the following keys: "mac_addr", "ip_addr", "interface". At the end of this process, you should have five dictionaries contained inside a single list. 

Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0

2a. Create a list where each of the list elements is a dictionary representing one of the network devices in the lab. Do this for at least four of the lab devices. The dictionary should have keys corresponding to the device_name, host (i.e. FQDN), username, and password. Use a fictional username/password to avoid checking the lab password into GitHub.

2b. Write the data structure you created in part 2a out to a YAML file. Use expanded YAML format. How could you re-use this YAML file later when creating Netmiko connections to devices?


3. NAPALM using nxos_ssh has the following data structure in one of its unit tests (the below data is in JSON format).  

{
    "Ethernet2/1": {
        "ipv4": {
            "1.1.1.1": {
                "prefix_length": 24
            }
        }
    },
    "Ethernet2/2": {
        "ipv4": {
            "2.2.2.2": {
                "prefix_length": 27
            }, 
            "3.3.3.3": {
                "prefix_length": 25
            }
        }
    }, 
    "Ethernet2/3": {
        "ipv4": {
            "4.4.4.4": {
                "prefix_length": 16
            }
        }, 
        "ipv6": {
            "fe80::2ec2:60ff:fe4f:feb2": {
                "prefix_length": 64
            }, 
            "2001:db8::1": {
                "prefix_length": 10
            }
        }
    }, 
    "Ethernet2/4": {
        "ipv6": {
            "fe80::2ec2:60ff:fe4f:feb2": {
                "prefix_length": 64
            }, 
            "2001:11:2233::a1": {
                "prefix_length": 24
            }, 
            "2001:cc11:22bb:0:2ec2:60ff:fe4f:feb2": {
                "prefix_length": 64
            }
        }
    } 
}
Read this JSON data in from a file.

From this data structure extract all of the IPv4 and IPv6 addresses that are used on this NXOS device. From this data create two lists: 'ipv4_list' and 'ipv6_list'. The 'ipv4_list' should be a list of all of the IPv4 addresses including prefixes; the 'ipv6_list' should be a list of all of the IPv6 addresses including prefixes.


4. You have the following JSON ARP data from an Arista switch:

{
    "dynamicEntries": 2,
    "ipV4Neighbors": [
        {
            "hwAddress": "dc38.e111.97cf",
            "address": "172.17.17.1",
            "interface": "Ethernet45",
            "age": 0
        },
        {
            "hwAddress": "90e2.ba5c.25fd",
            "address": "172.17.16.1",
            "interface": "Ethernet36",
            "age": 0
        }
    ],
    "notLearnedEntries": 0,
    "totalEntries": 2,
    "staticEntries": 0
}

From a file, read this JSON data into your Python program. Process this ARP data and return a dictionary where the dictionary keys are the IP addresses and the dictionary values are the MAC addresses. Print this dictionary to standard output.


5. In your lab environment, there is a file located at ~/.netmiko.yml. This file contains all of the devices used in the lab. Create a Python program that processes this YAML file and then uses Netmiko to connect to the Cisco3 router. Print out the router prompt from this device.

Note, the device dictionaries in the .netmiko.yml file use key-value pairs designed to work directly with Netmiko. The .netmiko.yml also contains group definitions for: cisco, arista, juniper, and nxos groups. These group definitions are lists of devices. Once again, don't check the .netmiko.yml into GitHub.


6. Use Netmiko to retrieve 'show run' from the Cisco4 device. Feed this configuration into CiscoConfParse.

Use CiscoConfParse to find all of the interfaces on Cisco4 that have an IP address. Print out the interface name and IP address for each interface. Your solution should work if there is more than one IP address configured on Cisco4. For example, if you configure a loopback interface on Cisco4 with an IP address, then your solution should continue to work. The output from this program should look similar to the following: 

$ python confparse_ex6.py 

Interface Line: interface GigabitEthernet0/0/0
IP Address Line:  ip address 10.220.88.23 255.255.255.0


7. You have the following BGP configuration from a Cisco IOS-XR router: 

router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out

From this BGP configuration, retrieve all of BGP peer IP addresses and their corresponding remote-as. Return a list of tuples. The tuples should be (neighbor_ip, remote_as). Print your data-structure to standard output.

Your output should look similar to the following. Use ciscoconfparse to accomplish this. 

BGP Peers: 
[('10.220.88.20', '42'), ('10.220.88.32', '43')]


Class 4.

- [ ] I.    Python Libraries and PIP 
- [ ] II.   sys.path and PYTHONPATH
- [ ] II.   __name__ Technique               
- [ ] IIV.  Reusing Code
- [ ] V.    TextFSM Overview 
- [ ] VI.   TextFSM Template Structure             
- [ ] VII.  TextFSM Creating a Template (Part1)           
- [ ] VIII. TextFSM Creating a Template (Part2)           
- [ ] IX    TextFSM Show Version Example        
- [ ] X.    TextFSM Filldown 


1. Using the following 'show interface status' output: 

Port      Name  Status       Vlan  Duplex Speed Type 
Gi0/1/0         notconnect   1     auto   auto  10/100/1000BaseTX
Gi0/1/1         notconnect   1     auto   auto  10/100/1000BaseTX
Gi0/1/2         notconnect   1     auto   auto  10/100/1000BaseTX
Gi0/1/3         notconnect   1     auto   auto  10/100/1000BaseTX

Create a TextFSM template that extracts only the 'Port' column (i.e. the interface name). The output of the FSM table should look as follows: 

$ textfsm.py ex1_show_int_status.tpl ex1_show_int_status.txt
...
FSM Table:
['PORT_NAME']
['Gi0/1/0']
['Gi0/1/1']
['Gi0/1/2']
['Gi0/1/3']


2. Expand the TextFSM template created in exercise1 such that you extract the Port, Status, Vlan, Duplex, Speed, and Type columns. For the purposes of this exercise you can ignore the 'Name' column and assume it will always be empty. The output of the FSM table should look similar to the following: 

$ textfsm.py ex2_show_int_status.tpl ex2_show_int_status.txt 
...
FSM Table:
['PORT_NAME', 'STATUS', 'VLAN', 'DUPLEX', 'SPEED', 'PORT_TYPE']
['Gi0/1/0','notconnect','1','auto','auto','10/100/1000BaseTX']
['Gi0/1/1','notconnect','1','auto','auto','10/100/1000BaseTX']
['Gi0/1/2','notconnect','1','auto','auto','10/100/1000BaseTX']
['Gi0/1/3','notconnect','1','auto','auto','10/100/1000BaseTX']


3. Using the 'show interface Ethernet2/1' output from nxos1 (see link below), extract the interface name, line status, admin state, MAC address, MTU, duplex, and speed using TextFSM.

https://github.com/ktbyers/pyplus_course/blob/master/class4/exercises/ex3_nxos_show_interface_ethernet_2_1.txt


4. Use TextFSM to parse the 'show arp' output from a Juniper SRX (see link below). Extract the following fields into tabular data: MAC Address, Address, Name, Interface.

https://github.com/ktbyers/pyplus_course/blob/master/class4/exercises/ex4_junos_show_arp.txt


5. Parse the 'show lldp neighbors' output from nxos1 (see link below). From this output use TextFSM to extract the Device ID, Local Intf, Capability, and Port ID.

https://github.com/ktbyers/pyplus_course/blob/master/class4/exercises/ex5_nxos_show_lldp_neighbors.txt


6. Parse the following 'show ip bgp summary' output (see link below). From this output, extract the following fields: Neighbor, Remote AS, Up_Down, and State_PrefixRcvd. Also include the Local AS and the BGP Router ID in each row of the tabular output (hint: use filldown for this). Note, in order to simplify this problem only worry about the data shown in the output (in other words, don't worry about all possible values that could be present in the output).

Second hint: remember there is an implicit 'EOF -> Record' at the end of the template (by default).

https://github.com/ktbyers/pyplus_course/blob/master/class4/exercises/ex6_show_ip_bgp_summary.txt


7. Using your TextFSM template and the 'show interface status' data from exercise2, create a Python program that uses TextFSM to parse this data. In this Python program, read the show interface status data from a file and process it using the TextFSM template. From this parsed-output, create a list of dictionaries. The program output should look as follows: 

$ python ex7_show_int_status.py 

[{'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/0',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/1',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/2',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/3',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'}]



