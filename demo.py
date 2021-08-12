import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="Narla",passwd="1234")

mycursor = mydb.cusor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)
