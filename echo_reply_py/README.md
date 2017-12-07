# Simple 'Echo Reply' scripts 

## Description 

To simple scripts to test communication between servers. 
I was suspecting 'rate limiting' on a client environment over a specific port. So I've built these two programs to test various rates of hundereds of client connections. 


# How to use 

* Clone the project 
* `echo_server.py` should run on your target host (as a server) by specifying a port for listening. Example:
```
python echo_server.py 135
```
* `echo_client.py' should run from the client side by specifying the target host and port. Example:
```
python echo_client.py SRPROD 135
```
* `launcher.sh` is used to run multiple client by specifying the number of clients (default is 20). Example to start 5000 clients:
```
./launcher.sh 5000
```

The script `echo_server.py` writes logs to the file `connections.log`. Example: 
`Connection from : ('172.24.192.10', 44972)`

The script `echo_client.py` writes logs to the file `resp.log`. Example of a successful Echo-Reply sequence:
`Resp OK : PID : 2415`

The script `launcher.sh` waits for 0.05 second after starting a client. You can adjust the command as you please.

__NB__: The scripts were built and used under python 2.7.5 on RedHat servers.

