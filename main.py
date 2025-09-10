import flask
import sqlite3
import hashlib
from flask import render_template, redirect, url_for
import datetime

#what to do
#add auto-refreshment
#add it for grade 9, 10 and 12
#try to add microsoft login

app=flask.Flask(__name__)
passwordHash='a82a9239452ee1f1772ed34876b9e149027d3ff8e7be2bf91979cf66b5e0ae90'

for grade in range(9,13):
    with sqlite3.connect('database.db') as database:
        cursor = database.cursor()
        cursor.execute(f'''
           CREATE TABLE IF NOT EXISTS logs{grade}(
           id INTEGER PRIMARY KEY AUTOINCREMENT, 
           classId INTEGER,
           amount INTEGER,
           submitText TEXT,
           addTime TEXT)
           ''')
        cursor.execute(f'''
           CREATE TABLE IF NOT EXISTS main{grade}(
           id INTEGER PRIMARY KEY AUTOINCREMENT, 
           name TEXT,
           score INTEGER)
           ''')
        cursor.execute(f'''
        SELECT * FROM main{grade}
        ''')
        if len(cursor.fetchall())==0:
            cursor.execute(f'INSERT INTO main{grade}(name, score) VALUES("{grade}A", 0);')
            cursor.execute(f'INSERT INTO main{grade}(name, score) VALUES("{grade}B", 0);')
            cursor.execute(f'INSERT INTO main{grade}(name, score) VALUES("{grade}C", 0);')
            cursor.execute(f'INSERT INTO main{grade}(name, score) VALUES("{grade}D", 0);')
            cursor.execute(f'INSERT INTO main{grade}(name, score) VALUES("{grade}E", 0);')
            cursor.execute(f'INSERT INTO main{grade}(name, score) VALUES("{grade}F", 0);')
        database.commit()


def checkPassword(password):
    if passwordHash==hashlib.sha256(password.encode("utf-8")).hexdigest():
        return True
    return False

@app.route('/')
def home():
    data=[]
    logs=[]
    """
    with sqlite3.connect('database.db') as database:
        cursor=database.cursor()
        cursor.execute('''
        SELECT score FROM main9;
        ''')
        scores=cursor.fetchall()
        scores=[score[0] for score in scores]
        cursor.execute('''
                       SELECT * FROM logs9;
                       ''')
        logs=cursor.fetchall()
        print(logs)
        #print(scores)"""
    for grade in range(9,13):
        with sqlite3.connect('database.db') as database:
            cursor=database.cursor()

            cursor.execute(f'''SELECT * FROM main{grade};''')
            data.append(cursor.fetchall())

            cursor.execute(f'''SELECT * FROM logs{grade};''')
            logs.append(cursor.fetchall())
    #print(data)
    print(logs)
    return render_template('newHome.html', data=data, logs=logs)

@app.route('/admin/')
def admin():
    #if request.method=='GET':
    data=[]
    for grade in range(9,13):
        with sqlite3.connect('database.db') as database:
            cursor = database.cursor()
            cursor.execute(f'''
            SELECT score FROM main{grade};
            ''')
            d=cursor.fetchall()
            #print(d)
            #data.append(list(map(lambda list: list[0], d)))
            data.append(list(map(lambda x: x[0],d)))

    print(data)
    return render_template('admin.html', data=data)

@app.route('/add/<grade>/<hmRm>/<amount>/<pas>/<submitMessage>', methods=['GET'])
def add(grade, hmRm, amount, pas, submitMessage):
    #rint(pas)
    #print(passwordHash)

    print('add')
    print('pas', checkPassword(pas))
    if not checkPassword(pas):
        print('add redirected home')
        return redirect(url_for("home"))

    time=datetime.datetime.now().strftime("%B %d")
    with sqlite3.connect('database.db') as database:
        cursor = database.cursor()
        cursor.executescript(f'''
        UPDATE main{grade} SET score = score + {amount} WHERE id={hmRm};
        
        
        INSERT INTO logs{grade}(classId, amount, submitText, addTime) VALUES("{hmRm}", "{amount}", "{submitMessage}", "{time}");
        ''')
        database.commit()
    return redirect(url_for("admin"))

@app.route('/checkPassword/<password>')
def anotherCheckPass(password):
    print(str(checkPassword(password)))
    return str(checkPassword(password))

@app.errorhandler(404)
def pageNotFound(e):
    print('ERROR PAGE NOT FOUND')#this is used for debugging purposes
    return redirect(url_for('home'))




app.run()