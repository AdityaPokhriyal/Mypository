import mysql.connector
mydb1 = mysql.connector.connect(host="localhost",user="root",passwd='password313')
#mycursor1 = mydb1.cursor()
#mycursor1.execute("create database HospitalAV")


mydb2 = mysql.connector.connect(host="localhost",user="root",passwd='password313',database='HospitalAV')
mycursor2 = mydb2.cursor()
#mycursor2.execute('''create table patients

                  #(patientID varchar(9) primary key NOT NULL,
                  
                  #name varchar(30) NOT NULL,
                  
                  #age int(3) NOT NULL,
                  
                  #disease_illness varchar(100) NOT NULL,
                  
                  #doctorname varchar(20) NOT NULL,
                  
                  #phonenumber varchar(20) NOT NULL,
                  
                  #address varchar(40) NOT NULL)''')'''

mycursor2.execute("select * from patients")

myresult = mycursor2.fetchall()

for i in myresult:
    print(i)



