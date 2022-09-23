# connection_checker
A python script that allows you to quickly check connectivity to a given network address and port.

** WORK IN PROGRESS **

## How to use the script ##

The script can either be run as a docker container or as standalone script.
The script is built using python3 standard modules and therefore does not have any dependencies.

Regardless of which method you use the run the script, the following environment variables must be provided.

### Export the following environment variables ###

1. `CONNECT_ADDRESS` (required): The ip address or hostname of the endpoint to connect to.
2. `CONNECT_PORT` (required): The TCP port number to connect to.
3. `CONNECT_TIMEOUT_SECS` (optional): The time in secs after which the connection will be terminated. *DEFAULT=3*
4. `CONNECT_LOG_LEVEL` (optional): The log level of script. *DEFAULT=INFO*

### Run the script ###

1. Clone the repo.

```text
➜  tmp git clone git@github.com:bosco-rodrigues/connection_checker.git
Cloning into 'connection_checker'...
remote: Enumerating objects: 11, done.
remote: Counting objects: 100% (11/11), done.
remote: Compressing objects: 100% (10/10), done.
remote: Total 11 (delta 1), reused 7 (delta 0), pack-reused 0
Receiving objects: 100% (11/11), done.
Resolving deltas: 100% (1/1), done.
➜  tmp
➜  tmp cd connection_checker
```

2. Export the environment variables

```text

➜  connection_checker git:(main) export CONNECT_ADDRESS='amazon.com'
➜  connection_checker git:(main) export CONNECT_PORT='443'
```

3. Run the script

```text

➜  connection_checker git:(main) python3 connection-checker/connect.py
09/23/2022 05:55:13 PM - 22 - main - INFO - Successfully connected to amazon.com on port 443
➜  connection_checker git:(main)
```

When running inside docker, make sure you pass the env variables using the -e option.

4. Docker build 

```
docker build -t connection-test .
docker tag connection-test <ecr-repo>
<ECR login>
docker push <ecr-repo>
```