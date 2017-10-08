import csv
from flask import Flask ,render_template , request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('homepage.html')

@app.route('/topUp',methods =['POST'])
def topUp():
    return render_template('page.html')

@app.route('/request',methods =['POST'])
def result():
    serialN = request.form['lastname']
    listSerial=read_file()
    check = 0
    for i in range(0,3) :
        if listSerial[i][0] == serialN :
            check = 1
            price = listSerial[i][1]
    if(check == 1 ) :
        return render_template('correct.html',serialN=serialN,price = price )
    else :
        return render_template('wrongPass.html',serialN=serialN)
    #serialN = request.form['serial']
    #return render_template('page2.htm  l',serialN)


def read_file():
    with open('static/SerialNumber.csv', 'r') as f:
      reader = csv.reader(f)
      my_list = list(reader)
    return(my_list)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
