Value INTERFACE (\S+)
Value STATUS (\S+)
Value VLAN (\d+)
Value DUPLEX (\S+)
Value SPEED (\S+)
Value PORT_TYPE (\S+\s*$$)

# Regex, match header and move state to 'ShowIPIntStatus' to start recording
Start
  ^Port.*Type\s*$$ -> ShowIPIntStatus

# 'INTERFACE' followed by 1 or more whitespace, followed by 'VLAN' etc..
ShowIPIntStatus
  ^${INTERFACE}\s+${STATUS}\s+${VLAN}\s+${DUPLEX}\s+${SPEED}\s+${PORT_TYPE} -> Record

# Overide implicit EOF record
EOF

# Copy of output string to be parsed, for easy reference.
#
#Port      Name  Status       Vlan  Duplex Speed Type 
#Gi0/1/0         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/1         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/2         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/3         notconnect   1     auto   auto  10/100/1000BaseTX

