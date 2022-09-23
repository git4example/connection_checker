# connection_checker
A python script that allows you to quickly check connectivity to a given network address and port.

** WORK IN PROGRESS **

## How to use ##

### Export the following environment variables ###

1. `CONNECT_ADDRESS` (required): The ip address or hostname of the endpoint to connect to.
2. `CONNECT_PORT` (required): The TCP port number to connect to.
3. `CONNECT_TIMEOUT_SECS` (optional): The time in secs after which the connection will be terminated. *DEFAULT=3*
4. `CONNECT_LOG_LEVEL` (optional): The log level of script. *DEFAULT=INFO*

### When running inside docker ###

1. Build the image `docker build -t connection-checker .`
2. 
