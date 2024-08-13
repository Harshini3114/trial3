import mysql.connector
conn=mysql.connector.connect(host='localhost',password='P@ce3114',user='root')

if conn.is_connected():
    print("Connection is made")
    
