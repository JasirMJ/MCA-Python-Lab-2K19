import mysql.connector

LOCALHOST = "localhost"
USER = "root"
PASSWORD = ""
DATABASE = "student"

cn=mysql.connector.connect(host=LOCALHOST,user=USER,passwd=PASSWORD,database=DATABASE)

mycursor = cn.cursor()
print("Database : ",DATABASE," connected sucessfully")
sql = "INSERT INTO details (name, age,course,place) VALUES ('Steve',23,'MCA','MLP')"
mycursor.execute(sql)
print("Record inserted sucessfully")
cn.commit()
print(mycursor.rowcount, "record inserted.")

