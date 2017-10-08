from flask import Flask , render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('data.html')

@app.route('/result' , methods = ['POST'])
def result():
	firstname = request.form['firstname']
	accountID = request.form['accountID']
	return render_template('data2.html',firstname = firstname,accountID = accountID)

@app.route('/choose' , methods = ['POST'])
def choose():
	return render_template('HTML_DEMO.html')

@app.route('/submit' , methods = ['POST'])
def submit():
	return render_template('transactioncomplete.html')


if __name__ == "__main__" :
 	app.run(host = "0.0.0.0" , debug=True)