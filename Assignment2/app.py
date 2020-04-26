#import pytesseract
import sqlite3
import os 
import json
import re
from flask import Flask, escape, request, send_from_directory, url_for, jsonify
#from PIL import Image
from werkzeug.utils import secure_filename
#from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

t_id = 1

UPLOAD_FOLDER = '/Users/mac/Documents/Python3.8.1/Assignment2/uploads'
ALLOWED_EXTENSIONS = set(['json'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def filename_setup(filename):
    return filename[-3:].lower() in ALLOWED_EXTENSIONS

def split(word):
    return [char for char in word]

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

@app.route('/')
def instruction():
    return f'enter /tests to start'

@app.route('/tests', methods = ['POST'])
def create_test():
    conn = sqlite3.connect("Tests.db")
    cursor = conn.cursor()
    #cursor.execute("DROP TABLE IF EXISTS TESTS")
    sql = '''CREATE TABLE IF NOT EXISTS tests(
    testid INTEGER, 
    subject TEXT, 
    answers TEXT
    )'''
    cursor.execute(sql)
    conn.commit()
    subject = request.get_json()['subject']
    answers = request.get_json()['answer_keys']
    global t_id 
    testid = t_id
    t_id += 1
    sql_insert = '''INSERT INTO tests (testid, subject, answers) VALUES (?, ?, ?)'''
    cursor.execute(sql_insert, (testid, subject, answers))
    conn.commit()
    #print(cursor.lastrowid)
    return {"test id": testid, "subject": subject, "answers": answers}, 201

@app.route('/tests/scantrons', methods = ['POST'])
def upload_scantron():
    scantron_id = request.form['scantron_id']
    file = request.files['file']
    testid = request.form['grade_by_test_id']
    tid = int(testid)
    #if file and filename_setup(file.filename):
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        with open(os.path.join(app.config['UPLOAD_FOLDER'], filename)) as f:
            data = json.load(f)
        #print(type(data))
        #print(data)
        conn = sqlite3.connect("Tests.db")
        cursor = conn.cursor()
        sql = '''SELECT answers FROM tests WHERE testid = ?'''
        cursor.execute(sql,(tid,))
        conn.commit()
        test_answers = cursor.fetchall()
        sql_1 = '''SELECT subject FROM tests WHERE testid = ?'''
        cursor.execute(sql_1,(tid,))
        conn.commit()
        subject = cursor.fetchall()
        subject = str(subject)
        subject = re.sub('[\W_]+', '', subject)
        test_answers = str(test_answers)
        filtered_answers = re.sub('[\W_]+', '', test_answers)
        test_answers_word = split(filtered_answers)
    
        #save scantron to sqlite3
        sql_s = '''CREATE TABLE IF NOT EXISTS scantrons(
        testid INTEGER,
        scantronid INTEGER,
        scantron TEXT,
        grade INTEGER
        )'''
        cursor.execute(sql_s)
        conn.commit()
        scantron = []
        scantron_data = data['answers']
        for item in scantron_data.values():
            scantron.append(item)
        scantron = listToString(scantron)
        scantron_id = int(scantron_id)
        #sql_scan = '''INSERT INTO scantrons (testid, scantronid, scantron) VALUES (?, ?, ?)'''
        #cursor.execute(sql_scan, (tid, scantron_id, scantron))
        #conn.commit()

        #grading algorithm
        grade = 0
        i = 0
        student_answers = data['answers']
        for a in student_answers.values():
            if a == test_answers_word[i]:
                grade += 1
            i += 1
        sql_scan = '''INSERT INTO scantrons (testid, scantronid, scantron, grade) VALUES (?, ?, ?, ?)'''
        cursor.execute(sql_scan, (tid, scantron_id, scantron, grade))
        conn.commit()

        #jsonify
        k = 0
        j = 1
        test_grade = []
        test_grade.append({'grade': grade, 'subject': subject, 'test_id': tid,})

        for b in student_answers.values():
            test_grade.append({
                'Question': j,
                'actual': b,
                'expected': test_answers_word[k] 
            })
            k += 1
            j += 1

        return jsonify(test_grade)
        #return "Upload successfully", 201
    else: 
        return "Upload failed", 500
    #file_J = request.files['file']
    #data = json.load(file_J)

@app.route('/tests/<tid>', methods = ['GET'])
def view_created_test(tid):
    test_id = int(tid)
    #scantronid = request.get_json()['scantron_id']
    conn = sqlite3.connect("Tests.db")
    cursor = conn.cursor()
    sql = '''SELECT * FROM tests WHERE testid = ?'''
    cursor.execute(sql,(test_id,))
    conn.commit()
    data = cursor.fetchall()
    for row in data:
        tid = row[0]
        subject = row[1]
        answers = row[2]
    return {"test id": tid, "subject": subject, "answers": answers}

@app.route('/tests/grades/<tid>', methods = ['GET'])
def grade_test(tid):
    test_id = int(tid)
    conn = sqlite3.connect("Tests.db")
    cursor = conn.cursor()
    sql = '''SELECT testid,subject,answers FROM tests WHERE testid = ?'''
    cursor.execute(sql,(test_id,))
    conn.commit()
    data = cursor.fetchall()
    for row in data:
        tid = row[0]
        subject = row[1]
        answers = row[2]
    answers = str(answers)
    answers = re.sub('[\W_]+', '', answers)
    answers = split(answers)

    sql_2 = '''SELECT scantronid,scantron,grade FROM scantrons WHERE testid = ?'''
    cursor.execute(sql_2,(test_id,))
    conn.commit()
    scan_data = cursor.fetchall()
    submission = []
    for row_s in scan_data:
        scantron_id = row_s[0]
        grade = row_s[2]
        submission.append({"test_id": test_id, "subject": subject, 'scantron_id': scantron_id, 'grade': grade, 'results':[]})
        scantron = row_s[1]
        scantron = str(scantron)
        scantron = re.sub('[\W_]+', '', scantron)
        scantron = split(scantron)
        #index = submission.index('results')
        for item in submission:
            for q, g in zip(scantron, answers):
                item["results"].append({"actual": q, "expected": g})
    return jsonify(submission)