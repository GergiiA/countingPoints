import flask
import sqlite3
import hashlib
from flask import render_template, request, redirect, url_for


app=flask.Flask(__name__)
passwordHash='a82a9239452ee1f1772ed34876b9e149027d3ff8e7be2bf91979cf66b5e0ae90'


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

@app.route('/add/<hmRm>/<amount>/<addition>/<pas>', methods=['GET', 'POST'])
def add(hmRm, amount, addition, pas):
    print(pas)
    print(passwordHash)
    print(hashlib.sha256(pas.encode("utf-8")).hexdigest())
    if passwordHash!=hashlib.sha256(pas.encode("utf-8")).hexdigest():
        return redirect(url_for("home"))

    with sqlite3.connect('database.db') as database:
        cursor = database.cursor()
        cursor.execute(f'''
        UPDATE main SET score = score {'+' if addition=="True" else '-'} {amount} WHERE id={hmRm}
        ''')

    return redirect(url_for("admin"))



app.run()