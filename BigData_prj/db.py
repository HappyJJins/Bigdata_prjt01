import mysql.connector

config={'user' : 'root',
        'password' : 'root',
        'host' : '127.0.0.1',
        'database' : 'bigdata_prjt',
        'port' : 3307}

def getConn():
    conn=mysql.connector.connect(**config)
    return conn