import csv
from flask import Flask ,render_template , request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('homepage.html')

@app.route('/topUp',methods =['POST'])
def topUp():
    return render_template('page.html',)

@app.route('/checkB',methods =['POST'])
def checkB():
    listAcc=read_file2()
    price = listAcc[1][2]
    #price = 55
    return render_template('checkBalance.html',price = price)

@app.route('/request',methods =['POST'])
def result():
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    serialN = request.form['lastname']
    listSerial=read_file()
    check = 0
    for i in range(0,3) :
        if listSerial[i][0] == serialN :
            check = 1
            price = listSerial[i][1]
            listAcc=read_file2()
            listAcc[1][2]  =  listAcc[1][2] + listSerial[i][1]


            
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
def read_file2():
    with open('static/Accounts.csv', 'r') as f:
      reader = csv.reader(f)
      my_list = list(reader)
    return(my_list)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
