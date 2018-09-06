# Question 1
import sqlite3
con = sqlite3.connect('Students.db')
print("connection is successful")
con.close()

# Question 2
# Question 3     //COMBINED 
import sqlite3
con = sqlite3.connect('Students.db')
cursor = con.cursor()
query = 'create table student_marks(name varchar(10),marks int(3))'
cursor.execute(query)
con.commit()
for i in range(1, 11):
    names = input("enter name")
    m = int(input("enter marks"))
    cursor.execute("insert into student_marks values(?, ?);", (names, m))
con.commit()
print("10 rows inserted successfully")

# Question 4
import sqlite3
con = sqlite3.connect('Students.db')
cursor = con.cursor()
query = 'select * from Student_marks where marks>80'
cursor.execute(query)
data = cursor.fetchall()
for row in data:
    print('name: {}, marks: {}' \
          .format(row[0], row[1]))
cursor.close()
con.close()
print('DONE!!!!')
