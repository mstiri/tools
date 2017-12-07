#!/usr/bin/env bash 

#
# Description: Spawn a number of clients that send a string to the server
# and expect it to resend it back
#

# Number of clients to start (Default: 20)
clients=${1:-20}

# Init responses file
echo "Start: $(date)" >resp.log
for i in $(seq $clients)
  do
    python echo_client.py SPROD 135 &
    # Wait 0.05 sec (50000 μs)
    usleep 50000
    echo -ne "\rclient $i / $clients   "
  done; echo ""

echo "End  : $(date)" >>resp.log
