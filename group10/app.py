from flask import Flask,render_template ,request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('instascan-master/docs/index.html')

@app.route('/result' , methods = ['POST'])
def result():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    return render_template('vs2.html', firstname = firstname, lastname = lastname)

if __name__ == "__main__":
    app.run(host = "0.0.0.0" , debug = True, use_reloader=False)
