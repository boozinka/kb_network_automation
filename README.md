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


Class 5.

- [ ] I.    Jinja2 Templating
- [ ] II.   Jinja2 Constructs
- [ ] III.  Jinja2 Variables
- [ ] IV.   Jinja2 Environment
- [ ] V.    Jinja2 Conditionals (Part1)
- [ ] VI.   Jinja2 Whitespace Stripping
- [ ] VII.  Jinja2 Conditionals (Part2)
- [ ] VIII. Jinja2 Nested Conditionals​
- [ ] IX.   Jinja2 Loops (Part1)​
- [ ] X.    Jinja2 Loops (Part2)
- [ ] XI.   Jinja2 Loop Nesting​
- [ ] XII.  Jinja2 Lists
- [ ] XIII. Jinja2 Dictionaries
- [ ] XIV.  Jinja2 Create Variables and Filters
- [ ] XV.   Jinja2 Includes​
- [ ] XVI.  Jinja2 Other Advanced Topics

1. Create a Python program that uses Jinja2 to generate the below BGP configuration. Your template should be directly embedded inside of your program as a string and should use for the following variables: local_as, peer1_ip, peer1_as, peer2_ip, peer2_as.

router bgp 10
  neighbor 10.1.20.2 remote-as 20
    update-source loopback99
    ebgp-multihop 2
    address-family ipv4 unicast
  neighbor 10.1.30.2 remote-as 30
    address-family ipv4 unicast


2a. Use Python and Jinja2 to generate the below NX-OS interface configuration. You should use an external template file and a Jinja2 environment to accomplish this. The interface, ip_address, and netmask should all be variables in the Jinja2 template.
 

nxos1
interface Ethernet1/1
  ip address 10.1.100.1/24

nxos2
interface Ethernet1/1
  ip address 10.1.100.2/24



2b. Expand your Jinja2 template such that both the following interface and BGP configurations are generated for nxos1 and nxos2. The interface name, IP address, netmask, local_as, and peer_ip should all be variables in the template. This is iBGP so the remote_as will be the same as the local_as.

nxos1

interface Ethernet1/1
  ip address 10.1.100.1/24

router bgp 22
  neighbor 10.1.100.2 remote-as 22
    address-family ipv4 unicast


nxos2

interface Ethernet1/1
  ip address 10.1.100.2/24

router bgp 22
  neighbor 10.1.100.1 remote-as 22
    address-family ipv4 unicast



2c. Use Netmiko to push the configurations generated in exercise 2b to the nxos1 device and to the nxos2 device, respectively. Verify you are able to ping between the devices and also verify that the BGP session reaches the established state. Note, you might need to use an alternate interface besides Ethernet 1/1 (you can use either Ethernet 1/1, 1/2, 1/3, or 1/4). Additionally, you might need to use a different IP network (to avoid conflicts with other students). Your autonomous system should remain 22, however.

For this exercise you should store your Netmiko connection dictionaries in an external file named my_devices.py and should import nxos1, and nxos2 from that external file. Make sure that you use getpass() to enter the password in for these devices (as opposed to storing the definitions in the file).

Note, this exercise gets a bit complicated when it is all said and done (templating, pushing configuration to devices, verifying the changes were successful).


3. Generate the following configuration output from an external Jinja2 template:

​vrf definition blue
 rd 100:1
 !
 address-family ipv4
  route-target export 100:1
  route-target import 100:1
 exit-address-family
 !
 address-family ipv6
  route-target export 100:1
  route-target import 100:1
 exit-address-family


Both the IPv4 and the IPv6 address families should be controlled by Jinja2 conditionals (in other words, the entire 'address-family ipv4' section and the entire 'address-family ipv6' sections can be dropped from the generated output depending on the value of two variables that you pass into your template--for example, the 'ipv4_enabled' and the 'ipv6_enabled' variables). Additionally, both the vrf_name and the rd_number should be variables in the template. Make sure that you control the whitespace in your output such that the configuration looks visually correct.


4. Expand on exercise3 except use a for-loop to configure five VRFs. Each VRF should have a unique name and a unique route distinguisher. Each VRF should once again have the IPv4 and the IPv6 address families controlled by a conditional-variable passed into the template.

Note, you will want to pass in a list or dictionary of VRFs that you loop over in your Jinja2 template.


5. Start with the full running-config from cisco3.lasthop.io as a base template (for example 'cisco3_config.j2'). Modify this base template such that you use Jinja2 include statements to pull in sub-templates for the NTP servers, the AAA configuration, and for the clock settings.

Your base template should have the following items (in the proper locations):

{% include 'aaa.j2' %}

{% include 'clock.j2' %}

{% include 'ntp.j2' %}


The child templates being pulled in should contain the NTP configuration, the AAA configuration, and the clock configuration. The two NTP servers, the timezone, timezone_offset, and timezone_dst (daylight savings timezone name) should be variables in these child templates.

The output from this should be the full configuration which is basically identical to the current running configuration on cisco3.blah.blah.


Class 6.

- [ ] I.    Arista eAPI Introduction
- [ ] II.   Arista eAPI Request Structure
- [ ] III.  Arista eAPI using Python-Requests Library
- [ ] IV.   Creating a Basic Connection using pyeapi
- [ ] V.    Creating Connections using pyeapi and .eapi.conf
- [ ] VI.   Executing Show Commands using pyeapi
- [ ] VII.  Configuring Devices using pyeapi
- [ ] VIII. Using the .api() method in pyeapi
- [ ] IX.   Arista eAPI Conclusion

1. Using the pyeapi library, connect to arista3.lasthop.io and execute 'show ip arp'. From this ARP table data, print out a mapping of all of the IP addresses and their corresponding MAC addresses.

2a. Define an Arista device in an external YAML file (use arista4.blah.blah for the device). In your YAML file, make sure the key names exactly match the names required for use with pyeapi and the connect() method. In other words, you should be able to execute 'connect(**device_dict)' where device_dict was retrieved from your YAML file. Do not store the lab password in this YAML file, instead set the password using getpass() in your Python program. Using this Arista device information stored in a YAML file, repeat the 'show ip arp' retrieval using pyeapi. Once again, from this ARP table data, print out a mapping of all of the IP addresses and their corresponding MAC addresses.

2b. Create a Python module named 'my_funcs.py'. In this file create two functions: function1 should read the YAML file you created in exercise 2a and return the corresponding data structure; function2 should handle the output printing of the ARP entries (in other words, create a separate function that handles all printing to standard out of the 'show ip arp' data). Create a new Python program based on exercise2a except the YAML file loading and the output printing is accomplished using the functions defined in my_funcs.py.

3. Using your external YAML file and your function located in my_funcs.py, use pyeapi to connect to arista4.lasthop.io and retrieve "show ip route". From this routing table data, extract all of the static and connected routes from the default VRF. Print these routes to the screen and indicate whether the route is a connected route or a static route. In the case of a static route, print the next hop address.

4. Note, this exercise might be fairly challenging. Construct a new YAML file that contains the four Arista switches. This YAML file should contain all of the connection information need to create a pyeapi connection using the connect method. Using this inventory information and pyeapi, create a Python script that configures the following on the four Arista switches:  

interface {{ intf_name }}
   ip address {{ intf_ip }}/{{ intf_mask }}

The {{ intf_name }} should be a Loopback interface between 1 and 99 (for example Loopback99).

The {{ intf_ip }} should be an address from the 172.31.X.X address space. The {{ intf_mask }} should be either a /24 or a /30.

Each Arista switch should have a unique loopback number, and a unique interface IP address.

You should use Jinja2 templating to generate the configuration for each Arista switch.

The data for {{ intf_name }} and for {{ intf_ip }} should be stored in your YAML file and should be associated with each individual Arista device. For example, here is what 'arista4' might look like in the YAML file:

arista4:
  transport: https
  host: arista4.blah.blah
  username: fred
  port: 443
  data:
    intf_name: Loopback99
    intf_ip: 172.31.1.13
    intf_mask: 30

Use pyeapi to push this configuration to the four Arista switches. Use pyeapi and "show ip interface brief" to display the IP address table after the configuration changes have been made.


Class 7.

- [ ] I.     XML - Why Care? 
- [ ] II.    XML Introduction
- [ ] III.   XML Terminology
- [ ] IV.    xmltodict Library 
- [ ] V.     xmltodict and the List Problem 
- [ ] VI.    xmltodict and Attributes
- [ ] VII.   Python-lxml Basics
- [ ] VIII.  Built-in XML Library and ElementTree 
- [ ] IX.    lxml and Traversing the XML Tree  
- [ ] X.     lxml and findall()
- [ ] XI.    XML and Namespaces 
- [ ] XII.   lxml and Handling Namespaces
- [ ] XIII.  NX-API Overview
- [ ] XIV.   NX-API and JSON-RPC
- [ ] XV.    NX-API and XML


1. Reading and accessing an XML file:

1a. Using the show_security_zones.xml file, read the file contents and parse the file using etree.fromstring(). Print out the newly created XML variable and also print out the variable's type. Your output should look similar to the following: 

<Element zones-information at 0x7f3271194b48>
<class 'lxml.etree._Element'>

1b. Using your XML variable from exercise 1a, print out the entire XML tree in a readable format (ensure that the output string is a unicode string).


1c. Print out the root element tag name (this tag should have a value of "zones-information"). Print the number of child elements of the root element (you can retrieve this using the len() function).


1d. Using both direct indices and the getchildren() method, obtain the first child element and print its tag name. 


1e. Create a variable named "trust_zone". Assign this variable to be the first "zones-security" element in the XML tree. Access this newly created variable and print out the text of the "zones-security-zonename" child.


1f. Iterate through all of the child elements of the "trust_zone" variable. Print out the tag name for each child element.


2. xmltodict basics

2a. Using xmltodict, load the show_security_zones.xml file as a Python dictionary. Print out this new variable and its type. Note, the newly created object is an OrderedDict; not a traditional dictionary.


2b. Print the names and an index number of each security zone in the XML data from Exercise 2a. Your output should look similar to the following (tip, enumerate will probably help): 

Security Zone #1: trust
Security Zone #2: untrust
Security Zone #3: junos-host


3. xmltodict: single vs multiple elements

3a. Open the following two XML files: show_security_zones.xml and show_security_zones_single_trust.xml. Use a generic function that accepts an argument "filename" to open and read a file. Inside this function, use xmltodict to parse the contents of the file. Your function should return the xmltodict data structure. Using this function, create two variables to store the xmltodict data structure from the two files.


3b. Compare the Python "type" of the elements at ['zones-information']['zones-security']. What is the difference between the two data types? Why?


3c. Optional - create a second function that uses xmltodict to read and parse a filename that you pass in. This function should support a "force_list" argument that is passed to xmltodict.parse(). Reminder, the force_list argument of xmltodict takes a dictionary where the dictionary key-name is the XML element that is required to be a list. For example:

force_list={"zones-security": True}

Use this new function to parse the "show_security_zones_single_trust.xml". Verify the Python data type is now a list for the ['zones-information']['zones-security'] element.


4. Use lxml to find() elements in an XML tree

4a. Use the find() method to retrieve the first "zones-security" element. Print out the tag of this element and of all its children elements. Your output should be similar to the following:

Find tag of the first zones-security element
--------------------
zones-security

Find tag of all child elements of the first zones-security element
--------------------
zones-security-zonename
zones-security-send-reset
zones-security-policy-configurable
zones-security-interfaces-bound
zones-security-interfaces


4b. Use the find() method to find the first "zones-security-zonename". Print out the zone name for that element (the "text" of that element).


4c. Use the findall() method to find all occurrences of "zones-security". For each of these security zones, print out the security zone name ("zones-security-zonename", the text of that element).


5. Dealing with Namespaces

Namespaces in XML help to differentiate between conflicting element names. 

5a. Load the show_version.xml file (originally from a Cisco NX-OS device) using the etree.fromstring() method. Note this XML document, unlike the previous documents, contains the document encoding information. Because the document encoding is at the top of the file, you will need to read the file using "rb" mode (the "b" signifies binary mode). Print out the the namespace map of this XML object. You can accomplish this by using the .nsmap attribute of your XML object.


5b. Similar to earlier exercises, use the find() method to access the text of the "proc_board_id" element (serial number). As this XML object contains namespace data, you will need to use the {*} namespace wildcard in the find() method. Your find call should look as follows:

find(".//{*}proc_board_id")

The {*} is a namespace wildcard and says to match ALL namespaces.


6. NX-API using json-rpc and the nxapi_plumbing library

6a. Create an nxapi_plumbing "Device" object for nxos1. The api_format should be "jsonrpc" and the transport should be "https" (port 8443). Use getpass() to capture the device's password. Send the "show interface Ethernet1/1" command to the device, parse the output, and print out the following information:

Interface: Ethernet1/1; State: up; MTU: 1500


7. NX-API using XML and the nxapi_plumbing library

7a. Create an nxapi_plumbing "Device" object for nxos1. The api_format should be "xml" and the transport should be "https" (port 8443). Use getpass() to capture the device's password. Send the "show interface Ethernet1/1" command to the device, parse the output, and print out the following information:

Interface: Ethernet1/1; State: up; MTU: 1500


7b. Run the following two show commands on the nxos1 device using a single method and passing in a list of commands: "show system uptime" and "show system resources". Print the XML output from these two commands.


7c. Using the nxapi_plumbing config_list() method, configure two loopbacks on nxos1 including interface descriptions. Pick random loopback interface numbers between 100 and 199.


Class 8.

- [ ] I.    NETCONF Overview
- [ ] II.   NETCONF and ncclient
- [ ] III.  Juniper PyEZ - Creating a Basic Connection
- [ ] IV.   Juniper PyEZ - Tables (Part1)
- [ ] V.    Juniper PyEZ - Tables (Part2)
- [ ] VI.   Juniper PyEZ - Configuration Basics 
- [ ] VII.  Juniper PyEZ - Config Changes from a File
- [ ] VIII. Juniper PyEZ - Configuration and XML
- [ ] IX.   Juniper PyEZ - RPC


1. PyEZ basic connection and facts:

1a. Create a PyEZ Device object from the jnpr.junos Device class. This device object should connect to "srx2.lasthop.io". Use getpass() to enter the device's password. Pretty print all of the device's facts. Additionally, retrieve and print only the "hostname" fact.


2. PyEZ Tables/Views:

2a. Create a Python module named jnpr_devices.py. This Python module should contain a dictionary named "srx2". This "srx2" dictionary should contain all of the key-value pairs needed to establish a PyEZ connection. You should use getpass() for the password handling. You should import this "srx2" device definition for all of the remaining exercises in class8.

2b. Create a Python program that creates a PyEZ Device connection to "srx2" (using the previously created Python module). Using this PyEZ connection and the RouteTable and ArpTable views retrieve the routing table and the arp table for srx2.

This program should have four separate functions:
1. check_connected() - Verify that your NETCONF connection is working. You can use the .connected attribute to check the status of this connection.
2. gather_routes() - Return the routing table from the device.
3. gather_arp_table() - Return the ARP table from the device.
4. print_output() - A function that takes the Juniper PyEZ Device object, the routing table, and the ARP table and then prints out the: hostname, NETCONF port, username, routing table, ARP table

This program should be structured such that all of the four functions could be reused in other class8 exercises.


3. PyEZ configuration operations (Part 1):

3a. Open a connection to the srx2 device and acquire a configuration lock. Validate that the configuration session is indeed locked by SSH'ing into the device and attempting to enter configuration mode ("configure"). Reuse, the 'srx2' device definition from the jnpr_devices.py file that you created in exercise2.

You should receive a prompt similar to the following: 

pyclass@srx2> configure
Entering configuration mode
Users currently editing the configuration:
  pyclass (pid 30316) on since 2019-03-08 18:30:51 PST
      exclusive

Add code to attempt to lock the configuration again. Gracefully handle the "LockError" exception (meaning the configuration is already locked).

3b. Use the "load" method to stage a configuration using a basic set command, for example, "set system host-name python4life".

3c. Print the diff of the current configuration with the staged configuration. Your output should look similar to the following: 

[edit system]
-  host-name srx2;
+  host-name python4life;

3d. Rollback the staged configuration. Once again, print out the diff of the staged and the current configuration (which at this point should be None).


4. PYeZ configuration operations (Part 2):

4a. Using the previously created jnpr_devices.py file, open a connection to srx2 and gather the current routing table information.

4b. Using PyEZ stage a configuration from a file. The file should be "conf" notation. This configuration should add two static host routes (routed to discard). These routes should be from the RFC documentation range of 203.0.113.0/24 (picking any /32 in that range should be fine). Use "merge=True" for this configuration. For example: 

routing-options {
    static {
        route 203.0.113.5/32 discard;
        route 203.0.113.200/32 discard;
    }
}

4c. Reusing your gather_routes() function from exercise2, retrieve the routing table before and after you configuration change. Print out the differences in the routing table (before and after the change). To simplify the problem, you can assume that the only change will be *additional* routes added by your script.

4d. Using PyEZ delete the static routes that you just added. You can use either load() and set operations or load() plus a configuration file to accomplish this.


5. PYeZ using direct RPC:

5a. Connect to the srx2 device. Using an RPC call, gather and pretty-print the "show version" information. Recall that you can retrieve RPC method name by running "show version | display xml rpc" argument. Also don't forget to convert the hyphens to underscores. Your output should match the following: 

<software-information>
<host-name>srx2</host-name>
<product-model>srx110h2-va</product-model>
<product-name>srx110h2-va</product-name>
<jsr/>
<package-information>
<name>junos</name>
<comment>JUNOS Software Release [12.1X46-D35.1]</comment>
</package-information>
</software-information>

5b. Using a direct RPC call, gather the output of "show interfaces terse". Print the output to standard out.

5c. Modify the previous task to capture "show interface terse", but this time only for "fe-0/0/7". Print the output to standard out. Use normalize=True in the RPC method call to make the output more readable. You will also need to add pretty_print=True to the etree.tostring() call. Consequently, your code should be similar to the following: 

xml_out = dev.rpc.get_interface_information(interface_name="fe-0/0/7", terse=True, normalize=True)
print(etree.tostring(xml_out, pretty_print=True, encoding="unicode"))


Class 9.

 - [ ] I.   NAPALM Overview​
 - [ ] II.  NAPALM - Simple Connection​
 - [ ] III. NAPALM - Getters
 - [ ] IV.  NAPALM - Configuration Merge
 - [ ] V.   NAPALM - Configuration Replace
 
 
 1. Simple NAPALM Connections and Facts

1a. Create a Python file named "my_devices.py" that defines the NAPALM connection information for both the 'cisco3' device and the 'arista1' device. Use getpass() for the password handling. This Python module should be used to store the device connection information for all of the exercises in this lesson.

1b. Create a simple function that accepts the NAPALM device information from the my_devices.py file and creates a NAPALM connection object. This function should open the NAPALM connection to the device and should return the NAPALM connection object.

1c. Using your "my_devices.py" file and your NAPALM connection function, create a list of NAPALM connection objects to 'cisco3' and 'arista1'.

1d. Iterate through the connection objects, print out the device's connection object itself. Additionally, pretty print the facts for each device and also print out the device's NAPALM platform type (ios, eos, et cetera).


2. NAPALM Getters

2a. Create a new file named "my_functions.py" that will store a set of reusable functions. Move the "open_napalm_connection" function from exercise1 into this Python file. Import the network devices once again from my_devices.py and create a list of connection objects (once again with connections to both cisco3 and arista1).

2b. Pretty print the arp table for each of these devices. Gather this information using the appropriate NAPALM Getter.

2c. Attempt to use the get_ntp_peers() method against both of the devices. Does this method work? Your code should gracefully handle any exceptions that occur. In other words, an exception that occurs due to this get_ntp_peers() method, should not cause the program to crash.

2d. Create another function in "my_functions.py". This function should be named "create_backup" and should accept a NAPALM connection object as an argument. Using the NAPALM get_config() method, the function should retrieve and write the current running configuration to a file. The filename should be unique for each device. In other words, "cisco3" and "arista1" should each have a separate file that stores their running configuration. Note, get_config() returns a dictionary where the running-config is referenced using the "running" key. Call this function as part of your main exercise2 and ensure that the configurations from both cisco3 and arista1 are backed up properly.


3. NAPALM Config Merge

3a. Using your existing functions and the my_devices.py file, create a NAPALM connection to both cisco3 and arista1.

3b. Create two new text files `arista1.lasthop.io-loopbacks` and `cisco3.lasthop.io-loopbacks`. In each of these files, create two new loopback interfaces with a description. Your files should be similar to the following:

interface loopback100
  description loopback100
!
interface loopback101
  description loopback101


For both cisco3 and arista1, use the load_merge_candidate() method to stage the candidate configuration. In other words, use load_merge_candidate() and your loopback configuration file to stage a configuration change. Use the NAPALM compare_config() method to print out the pending differences (i.e. the differences between the running configuration and the candidate configuration).

3c. Commit the pending changes to each device, and check the diff once again (after the commit_config).


4. Replace Operations

4a. Add nxos1 to your my_devices.py file. Ensure that you include the necessary information to set the NX-API port to 8443. This is done using 'optional_args' in NAPALM so you should have the following key-value pair defined:

​"optional_args": {"port": 8443}


4b. Create a new function named 'create_checkpoint'. Add this function into your my_functions.py file. This function should take one argument, the NAPALM connection object. This function should use the NAPALM _get_checkpoint_file() method to retrieve a checkpoint from the NX-OS device. It should then write this checkpoint out to a file.

Recall that the NX-OS platform requires a 'checkpoint' file for configuration replace operations. Using this new function, retrieve a checkpoint from nxos1 and write it to the local file system.

4c. Manually copy the saved checkpoint to a new file and add an additional loopback interface to the configuration.

4d. Create a Python script that stages a complete configuration replace operation (using the checkpoint file that you just retrieved and modified). Once your candidate configuration is staged perform a compare_config (diff) on the configuration to see your pending changes. After the compare_config is complete, then use the discard_config() method to eliminate the pending changes. Next, perform an additional compare_config (diff) to verify that you have no pending configuration changes. Do not actually perform the commit_config as part of this exercise.


