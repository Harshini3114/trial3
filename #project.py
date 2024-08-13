#project
import mysql.connector as my
db=my.connect(host="localhost",user="root",password="P@ce3114")
cursor=db.cursor()
cursor.execute("USE BUS;")
print("Welcome to Bus Booking")
f = input("FROM:")
t =input("TO:")
Query = "Select * from bus_booking where Start_From ='{}' and End_At ='{}'".format(f,t)
cursor.execute(Query)
c=cursor.fetchall()

print("BUS"," ","START"," ","END"," ","DEPARTURE"," ","ARRIVAL"," " ,"ID")
for i in c:
    print(i[0],"",i[1],"",i[2],"",i[3],"",i[4],"" ,i[5],)

a=input("Would you like to book tickets? Enter(yes/no)")
if a == "yes" or a == "YES":
    b= input("Enter bus_id:")
    cursor.execute("Select * from seat_availability where ID ='{}'".format(b))
    seat = cursor.fetchall()
    print("ID"," ","Seat Availability","  ","Type"," ","Seating"," ","Fare")
    for z in seat:
        print(z[0],"    ",z[1],"",z[2],"",z[3],"",z[4])
    ques=input("Would you like to confirm ticket? Enter(yes/no)")
    if ques == "yes" or ques =="YES":
        n=int(input("Number of passengers: "))
        fare=z[4]*n
        print("Total amount:",fare)
        name=input("ENTER YOUR NAME: ")
        phno=input("PLEASE ENTER YOUR 10-DIGIT PHONE NUMBER: ")
        email=input("ENTER YOUR EMAIL ID: ")
        address=input("ENTER YOUR ADDRESS: ")
        amount_paid=float(input("Enter amount to be paid:"))
        cursor.execute("""INSERT INTO USER_DETAILS VALUES(?,?,?,?,?)""",(name,phno,email,address,amount_paid))
        db.commit()
    


    
    
