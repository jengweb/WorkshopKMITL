import csv

from flask import Flask,render_template,request
app = Flask(__name__)

def findAvailableBalance(userID):

    amount = 0

    with open('userPaymentLimit.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            print(row)
            if row[0]== userID:
                paymentLimit = int(row[3])

    with open('expenses.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            print(row)
            if row[0] == userID:
                amount += int(row[4])

    percentAmount = 100-((paymentLimit-amount)*100/paymentLimit)

    print("ID",userID)
    print("PaymentLimit",paymentLimit,"THB")
    print("Use",amount,"THB")
    print(percentAmount,"%")
    return amount,paymentLimit,percentAmount

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/result',methods=['POST'])
def result():
    userID=request.form['userID']
    amount,paymentLimit,percentAmount=findAvailableBalance(userID)
    return render_template('LimitAlert.html',amount=amount,paymentLimit=paymentLimit,percentAmount=percentAmount)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
