from flask import Flask
from flask import request
from flask import render_template
import csv

app = Flask(__name__)


# @app.route('/login/<name>', methods=['GET', 'POST'])
# def user(name):
    # if request.method == 'POST':
        # return 'POST %s' % name
    # else:
        # return 'GET %s' % name
@app.route('/transaction')
def transaction():
    data = []
    with open('transaction.csv', 'r') as f:
        reader = csv.reader(f)

        for i, n in enumerate(reader):
            if i != 0:
                data.append(n)

    return render_template('transaction.html', data=data)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def auth():
    #fetch user
    id = request.form['id']
    password = request.form['password']

    #find user from id
    data = []
    result = False
    with open('profile.csv', 'r') as f:
        reader = csv.reader(f)

        for i, n in enumerate(reader):
            if i != 0:
                data.append(n)
        for i, n in enumerate(data):
            if data[i][0] == id:
                result = True

        if result == True:
            return redirect("/transaction", code=200)
        else:
            return redirect("/login")

@app.route('/hello/')
def hello():
    return render_template('hello.html')

