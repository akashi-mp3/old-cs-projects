#Team Red Squadron
#Lorenz "Red 2" Vargas and Winston "Luke's Friend from Tatooine" Venderbush

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O



f="schoolinfo.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================

# with open('peeps.csv') as csvfile1:
# 	peeps = csv.DictReader(csvfile1)

# with open('courses.csv') as csvfile2:
# 	courses = csv.DictReader(csvfile2)
# 	for row in courses:
# 		print(row['code'], row['mark'], row['id'])

#db.close()


q = "CREATE TABLE students (name TEXT, age INTEGER, id INTEGER)"
c.execute(q)    
q = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)"
c.execute(q)
fObj1 = open("peeps.csv")
fObj2 = open("courses.csv") 
peeps = csv.DictReader(fObj1)
courses = csv.DictReader(fObj2)

for k in peeps:
    p = "INSERT INTO students VALUES (" + "'" + k['name'] + "'" + "," + "'" + k['age'] + "'" + "," + "'" + k['id'] + "'" + ")"
    c.execute(p)

for j in courses:
    r = "INSERT INTO courses VALUES (" + "'" + j['code'] + "'" + "," + "'" + j['mark'] + "'" + "," + "'" + j['id'] + "'" + ")"
    c.execute(r)



#==========================================================
db.commit() #save changes
db.close()  #close database
