from flask import Flask , render_template , request
from donate import donate
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('Donate_Detail.html')

@app.route('/result' , methods=['POST'])
def result():
    donate_id = request.form['donate_id']
    donate_money = request.form['donate_money']
    account_id = "58010781"
    isdonate = donate(donate_id,account_id,donate_money)
    if(isdonate==True):
        return render_template('page2.html',donate_id=donate_id, donate_money=donate_money , account_id = account_id)
    else:
        return render_template('page2.html',donate_id="Can't", donate_money="Donate" , account_id = "This event")


#@app.route('/result' , methods=['POST'])
#def result():
#    firstname = request.form['firstname']
#    lastname = request.form['lastname']
#    return render_template('page2.html',firstname=firstname, lastname=lastname)

#@app.route('/Donate_detail' , methods=['POST'])
#def Donate_detail();

if __name__ == '__main__':
    app.run(host="0.0.0.0" , debug=True)
