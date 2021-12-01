# Varible containing Regex to match 1 or more non-whitespace
Value INTERFACE (\S+)

# Regex to match the header and move the state to 'ShowIPIntStatus
Start
  ^Port.*Type\s*$$ -> ShowIPIntStatus

# Use the 'INTERFACE' varible to start recording
ShowIPIntStatus
  ^${INTERFACE} -> Record
  
# Overide implicit EOF Record with my own EOF
EOF

# Copy of the string file for easy reference
#
#Port      Name  Status       Vlan  Duplex Speed Type 
#Gi0/1/0         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/1         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/2         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/3         notconnect   1     auto   auto  10/100/1000BaseTX
 
