import mysql.connector as my
db=my.connect(host="localhost",user="root",password="P@ce3114")
cursor=db.cursor()
cursor.execute("USE BUS;")
print("Welcome to Bus Booking")
t = input("TO:")
f=input("FROM:")
Query = "Select * from bus_booking where Start_From ='{}' and End_At ='{}'".format(t,f)
cursor.execute(Query)
c=cursor.fetchall()

print("BUS"," ","START"," ","END"," ","DEPARTURE"," ","ARRIVAL"," " ,"ID")
for i in c:
    print(i[0],"",i[1],"",i[2],"",i[3],"",i[4],"" ,i[5],)
db.close()
