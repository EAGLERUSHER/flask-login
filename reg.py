from distutils.log import debug
from multiprocessing import connection
import sqlite3
from flask import Flask,render_template,request,url_for, session
import re
from flask import render_template

app=Flask(__name__)
app.secret_key = '__privatekey__'
connection =sqlite3.connect("user1.db")
cursor = connection.cursor()


@app.route('/')
def test():
    connection =sqlite3.connect("user1.db")
    cursor = connection.cursor()
    return render_template("index.html")
@app.route('/index', methods =['GET', 'POST'])
def home():
    connection =sqlite3.connect("user1.db")
    cursor = connection.cursor()
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        
        cursor.execute('SELECT * FROM users WHERE emailaddress = ? AND password = ?', (email, password))
        account = cursor.fetchone()
        if account:
            # session['loggedin'] = True
            session['email'] = account[1]
            session['password'] = account[3]
            msg = 'Logged in successfully !'
            print(msg)
            return render_template('res.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
            print(msg)
            return render_template('error.html', msg = msg)
    return render_template('index.html', msg = msg)
    

@app.route('/Register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'name' in request.form and 'email-address' in request.form and'password' in request.form :
        name = request.form['name']
        Email = request.form['email-address']
        Password = request.form['password']
        
        
        
        
        con =sqlite3.connect("user1.db")
        cursor = con.cursor()
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute('SELECT * FROM users WHERE username = % s', (username, ))
        chk=f"SELECT * FROM users WHERE name = '{name}'  AND emailaddress='{Email}' AND password='{Password}'"
        cursor.execute(chk)
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', Email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', Password):
            msg = 'Username must contain only characters and numbers !'
        elif not name or not Password or not Email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO users VALUES (?, ?, ?)', (name, Email,Password))
            con.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('Register.html', msg = msg)


   

    


connection.commit()

if __name__=="__main__":
    app.run(debug=True)