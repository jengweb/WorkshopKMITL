from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def hello():
   return render_template('hello.html')

@app.route('/insert_profile', methods=['POST'])
def insert_profile():
    name = request.form['name']
    lastname = request.form['lastname']
    with open('names.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, lastname])

    with open('names.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        return render_template('result.html', reader=reader)

def FizzBuzz(number):
    return number

if __name__ == "__main__":
   app.run(host="0.0.0.0", debug=True)
