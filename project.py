import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                         database='bus',
                                         user='root',
                                         password='P@ce3114')
if connection.is_connected():
    print("true")
else:
    print("false")

# Printing the connection object
n = input("From:")
m= input("To:")
Query= "Select * from bus_booking where Start_From = {} and End_At = {}".format(n,m)
cursor=connection.cursor()
cursor.execute(Query)
res=cursor.fetchall()
for i in res:
    print (i)
    
