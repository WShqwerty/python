import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Wsh.123456",
    database = "work_test1"
)

mycursor = mydb.cursor()

sql = "select * from student"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)