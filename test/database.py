import sqlite3
from flask import Flask, escape, request
app = Flask(__name__)
'''
@app.route('/')

conn = sqlite3.connect('lab2databse')
c = conn.cursor()
c.execute('DROP TABLE IF exists students')
c.execute("""CREATE TABLE students(
            id INTEGER PRIMARY KEY,
            name TEXT
)""")
print("Student Table Created")

c.execute('DROP TABLE IF exists class')
c.execute("""CREATE TABLE class(
            id INTEGER PRIMARY KEY,
            c_name TEXT,
            students TEXT
)""")
print("Class Table Created")

c.execute("INSERT INTO students VALUES ('777', 'Rain')")
c.commit()
c.execute("INSERT INTO class VALUES ('787', 'CMPE273', 'Rain')")
c.commit()

c.execute("select * from students")
rows = c.fetchall()
print(rows)
conn.close() 
'''

@app.route('/')
def hello():

    uListStr = ""
    sqliteDB = sqlite3.connect(DATABASE)
    print ("Opened database successfully")
    sqliteDB.execute('DROP TABLE IF exists students')
    sqliteDB.execute('CREATE TABLE students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, addr TEXT, city TEXT, pin TEXT)')
    print ("Table created successfully")

    cur = sqliteDB.cursor()
    cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",('wan', '99', 'san', '1111'))

    sqliteDB.commit()

    #sqliteDB.row_factory = sql.Row
    cur = sqliteDB.cursor()
    cur.execute("select * from students")
    rows = cur.fetchall()
    print(rows)
    sqliteDB.close()

    return "hello"