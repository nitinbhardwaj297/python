import mysql.connector

mydb = mysql.connector.connect (
        host = "localhost",
        user = "root",
        password = "Nitin@123"
)

cursor = mydb.cursor()
cursor.execute("use project1")




