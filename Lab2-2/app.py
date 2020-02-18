from flask import Flask, escape, request
import sqlite3
from collections import defaultdict

#DATABASE='db.db'
app = Flask(__name__)

s_id = 1
c_id = 1000

students = {"student_id": "student_name"}
#classes = {"class_id": {"class_name": {"student_id": "student_name"}}}
classes = {"class_id": "class_name"}
student_class = {"class_id": {"student_id": "student_name"}}


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
'''
def test():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    conn.execute('DROP TABLE IF exists students')
    conn.execute("""CREATE TABLE students(
                id INTEGER PRIMARY KEY,
                name TEXT
    )""")
    print("Student Table Created")

    conn.execute('DROP TABLE IF exists class')
    conn.execute("""CREATE TABLE class(
                id INTEGER PRIMARY KEY,
                c_name TEXT,
                students TEXT
    )""")
    print("Class Table Created")

    conn.execute("INSERT INTO students VALUES ('777', 'Rain')")
    conn.commit()
    conn.execute("INSERT INTO class VALUES ('787', 'CMPE273', 'Rain')")
    conn.commit()

    c.execute("select * from students")
    rows = c.fetchall()
    print(rows)
    conn.close() 
    return "hello"
'''


@app.route('/students', methods = ['POST'])
def create_student():
    name = request.get_json()['name']
    #data = request.get_json()
    #name = data['name']
    global s_id
    s_id += 1
    students.update({s_id : name})
    return {"id": s_id, "name": name}, 201

@app.route('/students/<sid>', methods = ['GET'])
def get_student(sid):
    #student_id = request.args.get("sid")
    #print(type(sid))
    sid = int(sid)
    name = students.get(sid)
    return {"id": sid, "name": name}

@app.route('/classes', methods = ['POST'])
def create_class():
    c_name = request.get_json()['name']
    global c_id
    c_id += 1
    classes.update({c_id: c_name})
    student_class[c_id] = {}
    return {"class id": c_id, "class name": c_name}, 201

@app.route('/classes/<cid>', methods = ['GET'])
def get_class(cid):
    cid = int(cid)
    c_name = classes.get(cid)
    return {"class id": cid, "class name": c_name}

@app.route('/classes/<cid>', methods = ['PATCH'])
def add_student_class(cid):
    cid = int(cid)
    c_name = classes.get(cid)
    student_id = request.get_json()["sid"]
    student_id = int(student_id)
    student_name = students.get(student_id)
    student_class[cid].update({student_id: student_name})
    #classes[cid][c_name].update({student_id: student_name})
    print(student_class)
    return {"class id": cid, "class name": c_name, "student id": student_id, "student name": student_name}
