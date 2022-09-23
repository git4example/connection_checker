from operator import truediv
import os
import logging
import socket
import time

address = os.getenv("CONNECT_ADDRESS")
port = int(os.getenv("CONNECT_PORT"))
timeout = int(os.getenv('CONNECT_TIMEOUT_SECS', default=3))
log_level = os.getenv("CONNECT_LOG_LEVEL", default="INFO")

log = logging.getLogger('connect_check.py')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(lineno)s - %(funcName)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p'))
log.addHandler(handler)
log.setLevel(log_level)


def main():
    i = 1
    while i:
        s = socket.socket()
        try:
            s.settimeout(timeout)
            s.connect((address, port))
            log.info(f'Successfully connected to {address} on port {port}')
        except Exception as e:
            log.error(f"Failed trying to connect to {address} on port {port}. Exception is {e}")
        finally:
            s.close()
        time.sleep(1)

if __name__ == '__main__':
    main()
