import socket
import sys

def usage():
    print '\nUsage: python %s listeningrPort' % sys.argv[0]
    print '          - listeningrPort: TCP Port to listen on\n'
    exit()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tell the kernel to reuse the port even if it is in TIME_WAIT state 
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) == 2:
    host = ''
    port = int(sys.argv[1])
else:
    usage()
server_address = (host, port)
# Bind the socket to the port
print 'Start listening on port: %s' % port
sock.bind(server_address)

# Connections log 
conn_log = open('connections.log', 'w', buffering=0)

# Listen for incoming connections
# I set it to my kernel value of net.ipv4.tcp_max_syn_backlog: 2048
sock.listen(2048)

try:
    while True:
        # Wait for incoming connection
        connection, client_address = sock.accept()
        print >>conn_log, 'Connection from :', client_address
        try:
            # Receive data
            data = connection.recv(128)
            # Send back received data
            connection.sendall(data)
    
        finally:
            # Close connection
            connection.close()
    
except KeyboardInterrupt, SystemExit:
    print 'Closing file before quitting'
    conn_log.close()


