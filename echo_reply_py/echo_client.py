import socket
import sys
import os
from datetime import datetime
import time

def usage():
    print '\nUsage: python %s serverIP serverPort' % sys.argv[0]
    print '          - serverIP  : IP address or hostname of the remote server'
    print '          - serverPort: TCP Port of the remote server\n'
    exit()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) == 3:
    server_name = str(sys.argv[1])
    server_port = int(sys.argv[2])
else:
    usage()

server_address = (server_name, server_port)
# Connect the socket to the port where the server is listening
sock.connect(server_address)

# Respones log
resp_log = open('resp.log', 'a')

try:
    # Get current time
    ts = datetime.now().strftime("%H:%M:%S.%f")
    # Get PID
    client_pid = os.getpid()
    # Build message 
    message = str(ts) + ' PID: ' + str(client_pid)
    # Send message
    sock.sendall(message)
    # Look for the response
    data = sock.recv(128)
    sock.close()
    if data == message:
        print >>resp_log, 'Resp OK : PID : %s ' % client_pid
    else:
        print >>resp_log, 'Resp KO : PID : %s data: [%s]' % (client_pid, data)

finally:
    sock.close()

resp_log.close()
