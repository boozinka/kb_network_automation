Value INT_NAME (Ethernet\S+)
Value LINE_STATUS (up|down)
Value ADMIN_STATUS (up|down)
Value MAC_ADDR ([0-9a-fA-F]{4}\.[0-9a-fA-F]{4}\.[0-9a-fA-F]{4})
Value MTU_VALUE ([0-9]{4})
Value DUPLEX (\S+duplex)
Value SPEED (\d+\s\S+$$)

Start
  ^${INT_NAME} is ${LINE_STATUS}
  ^admin state is ${ADMIN_STATUS}
  ^.*address:\s${MAC_ADDR}
  ^\s+MTU ${MTU_VALUE}
  ^\s+${DUPLEX},\s+${SPEED} -> Record

EOF

