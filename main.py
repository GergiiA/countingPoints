import flask
import sqlite3
import hashlib
from flask import render_template, redirect, url_for
import datetime


app=flask.Flask(__name__)
passwordHash='a82a9239452ee1f1772ed34876b9e149027d3ff8e7be2bf91979cf66b5e0ae90'

with sqlite3.connect('database.db') as database:
    cursor = database.cursor()
    cursor.execute('''
       CREATE TABLE IF NOT EXISTS logs(
       id INTEGER PRIMARY KEY AUTOINCREMENT, 
       classId INTEGER,
       amount INTEGER,
       submitText TEXT,
       addTime TEXT)
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
    database.commit()


def checkPassword(password):
    if passwordHash==hashlib.sha256(password.encode("utf-8")).hexdigest():
        return True
    return False

@app.route('/')
def home():
    with sqlite3.connect('database.db') as database:
        cursor=database.cursor()
        cursor.execute('''
        SELECT score FROM main;
        ''')
        scores=cursor.fetchall()
        scores=[score[0] for score in scores]
        cursor.execute('''
                       SELECT * FROM logs;
                       ''')
        logs=cursor.fetchall()
        print(logs)
        #print(scores)
    return render_template('newHome.html', scores=scores, logs=logs)

@app.route('/admin/')
def admin():
    #if request.method=='GET':
    with sqlite3.connect('database.db') as database:
        cursor = database.cursor()
        cursor.execute('''
        SELECT score FROM main;
        ''')
        scores = cursor.fetchall()
    return render_template('admin.html', scores=scores)

@app.route('/add/<hmRm>/<amount>/<pas>/<submitMessage>', methods=['GET', 'POST'])
def add(hmRm, amount, pas, submitMessage):
    #rint(pas)
    #print(passwordHash)

    print('add')
    if not checkPassword(pas):
        print('add redirected home')
        return redirect(url_for("home"))

    time=datetime.datetime.now().strftime("%B %d")
    with sqlite3.connect('database.db') as database:
        cursor = database.cursor()
        cursor.executescript(f'''
        UPDATE main SET score = score + {amount} WHERE id={hmRm};
        
        
        INSERT INTO logs(classId, amount, submitText, addTime) VALUES("{hmRm}", "{amount}", "{submitMessage}", "{time}");
        ''')
        database.commit()

    return redirect(url_for("admin"))

@app.route('/checkPassword/<password>')
def anotherCheckPass(password):
    print(str(checkPassword(password)))
    return str(checkPassword(password))

@app.errorhandler(404)
def pageNotFound(e):
    return redirect(url_for('home'))



app.run()