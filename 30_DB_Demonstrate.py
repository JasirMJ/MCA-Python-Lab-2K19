import mysql.connector

LOCALHOST = "localhost"
USER = "root"
PASSWORD = ""
DATABASE = "student"

cn=mysql.connector.connect(host=LOCALHOST,user=USER,passwd=PASSWORD,database=DATABASE)

mycursor = cn.cursor()
print("Database : ",DATABASE," connected sucessfully")
sql = "INSERT INTO details (name, age,course,place) VALUES " \
      "('Steve',23,'MCA','MLP')," \
      "('Ahamed',22,'MCA','EKM')," \
      "('Ravi',24,'MCA','TCR')"

mycursor.execute(sql)
print("Record inserted sucessfully")
print(mycursor.rowcount, "record inserted.")

select = "SELECT * FROM details"
mycursor.execute(select)

result = mycursor.fetchall()

print("Name\t","Age\t","Course\t","Place")
for x in result:
    name = x[1]
    age = x[2]
    course = x[3]
    place = x[4]
    print(name,"\t",age,"\t",course,"\t",place)