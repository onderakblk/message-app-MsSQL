import pyodbc

def create():
    server = 'DESKTOP-NTCB8R5\MSSQLSERVERR'
    database = 'master'
    username = 'sa'
    password = '351880Oo.'

    connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    conn = pyodbc.connect(connection_string, autocommit=True)
    cursor = conn.cursor()

    cursor.execute('EXEC(\'CREATE DATABASE message\')')

    conn.close()



def tables():
    server = 'DESKTOP-NTCB8R5\MSSQLSERVERR'
    database= 'message'
    username = 'sa'
    password = '351880Oo.'

    connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    cursor.execute('CREATE TABLE users (id INT IDENTITY(1,1) PRIMARY KEY, username_ VARCHAR(50), password_ VARCHAR(50), name VARCHAR(50), surname VARCHAR(50), email VARCHAR(50), number VARCHAR(50))')
    cursor.close()
    cursor1 = conn.cursor()
    cursor1.execute('CREATE TABLE mesage (id INT IDENTITY(1,1) PRIMARY KEY, sender VARCHAR(50), buyer varchar(50), message varchar(150))')
    cursor1.close()
    conn.commit()
    conn.close()

create()
tables()