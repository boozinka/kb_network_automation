Value Filldown ROUTER_ID ([0-9\.]+)
Value Filldown LOCAL_AS (\d+)
Value NEIGHBOR ([0-9\.]+)
Value REMOTE_AS (\d+)
Value UP_DOWN (\w+)
Value STATE_PFX_RCD (\w+)

Start
  ^BGP router\s\S+\s+${ROUTER_ID}.+AS number\s${LOCAL_AS}.*$$
  ^Neighbor.*PfxRcd.*$$ -> BGPNeiTable

BGPNeiTable
  ^${NEIGHBOR}\s+\d+\s+${REMOTE_AS}[\s+\d+\s+]+${UP_DOWN}\s+${STATE_PFX_RCD}.*$$ -> Record

EOF

# Copy of output string to be parsed, for easy reference.
#
#Capability codes:
#  (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
#  (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other
#Device ID                         Local Intf          Hold-time   Capability  Port ID     
#nxos2.twb-tech.com                Eth2/1              120          BR          Eth2/1      
#nxos2.twb-tech.com                Eth2/2              120          BR          Eth2/2      
#nxos2.twb-tech.com                Eth2/3              120          BR          Eth2/3      
#nxos2.twb-tech.com                Eth2/4              120          BR          Eth2/4      
#Total entries displayed: 4
