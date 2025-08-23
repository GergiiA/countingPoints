import flask
import sqlite3
import hashlib
from flask import render_template, request, redirect, url_for


app=flask.Flask(__name__)
passwordHash='a82a9239452ee1f1772ed34876b9e149027d3ff8e7be2bf91979cf66b5e0ae90'

with sqlite3.connect('database.db') as database:
    cursor = database.cursor()
    cursor.execute('''
       CREATE TABLE IF NOT EXISTS logs(
       id INTEGER PRIMARY KEY AUTOINCREMENT, 
       classId INTEGER,
       amount INTEGER)
       ''')
    cursor.execute('''
       CREATE TABLE IF NOT EXISTS main(
       id INTEGER PRIMARY KEY AUTOINCREMENT, 
       name TEXT,
       score INTEGER)
       ''')
    cursor.execute('''
    SELECT * FROM main
    ''')
    if len(cursor.fetchall())==0:
        cursor.execute('INSERT INTO main(name, score) VALUES("11A", 0);')
        cursor.execute('INSERT INTO main(name, score) VALUES("11B", 0);')
        cursor.execute('INSERT INTO main(name, score) VALUES("11C", 0);')
        cursor.execute('INSERT INTO main(name, score) VALUES("11D", 0);')
        cursor.execute('INSERT INTO main(name, score) VALUES("11E", 0);')
        cursor.execute('INSERT INTO main(name, score) VALUES("11F", 0);')


@app.route('/')
def home():
    with sqlite3.connect('database.db') as database:
        cursor=database.cursor()
        cursor.execute('''
        SELECT score FROM main;
        ''')
        scores=cursor.fetchall()
        scores=[score[0] for score in scores]
        print(scores)
    return render_template('main.html', scores=scores)



@app.route('/admin', methods=['GET'])
def admin():
    if request.method=='GET':
        with sqlite3.connect('database.db') as database:
            cursor = database.cursor()
            cursor.execute('''
            SELECT score FROM main;
            ''')
            scores = cursor.fetchall()
        return render_template('admin.html', scores=scores)
    return 0

@app.route('/add/<hmRm>/<amount>//<pas>', methods=['GET', 'POST'])
def add(hmRm, amount, pas):
    #rint(pas)
    #print(passwordHash)
    #print(hashlib.sha256(pas.encode("utf-8")).hexdigest())
    if passwordHash!=hashlib.sha256(pas.encode("utf-8")).hexdigest():
        return redirect(url_for("home"))

    with sqlite3.connect('database.db') as database:
        cursor = database.cursor()
        cursor.execute(f'''
        UPDATE main SET score = score + {amount} WHERE id={hmRm}
        ''')
        cursor.execute(f'''
        INSERT INTO logs(classId, amount) VALUES({hmRm}, {amount})
        ''')

    return redirect(url_for("admin"))



app.run()