import pyodbc
server = 'tcp:csucla2015.database.windows.net'
database = 'AdventureWorks'
username = 'meet_bhagdev'
password = 'avengersA1'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print row
    row = cursor.fetchone()
