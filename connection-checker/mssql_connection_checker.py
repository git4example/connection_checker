import os
import logging

import pyodbc

address = os.getenv('MSSQL_SERVER_ADDRESS')
#port = int(os.getenv('MSSQL_SERVER_PORT', default=1443))
port = os.getenv('MSSQL_SERVER_PORT', default=1443)

server = f'tcp:{address}'
database = os.getenv('MSSSQL_DATABASE')
username = os.getenv('MSSQL_USERNAME')
password = os.getenv('MSSQL_PASSWORD')

log_level = os.getenv("CONNECT_LOG_LEVEL", default="INFO")

log = logging.getLogger('connect_check.py')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(lineno)s - %(funcName)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p'))
log.addHandler(handler)
log.setLevel(log_level)


def get_connection():
    connection = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
    cursor = connection.cursor()
    return cursor


def get_version(cursor):
    cursor.execute("SELECT @@version;")
    row = cursor.fetchone()
    while row:
        log.info('Row: %s' % row[0])
        row = cursor.fetchone()
        return row


def main():
    connection = get_connection()
    version = get_version(cursor=connection)

    log.info('MSSQL Version: %s' % version)


if __name__ == '__main__':
    main()