import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "Nitin",
    password = "Nitin@123",
    database = "Nitindb"
)

cursor = connection.cursor()

cursor.execute("select * from person")
results = cursor.fetchall()

for i in results:
    print(i)

