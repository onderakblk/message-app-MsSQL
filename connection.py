import pyodbc


server = 'yourserver'
database = 'message'
username = 'yourusername'
password = 'yourpassword'

connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

   