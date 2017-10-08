from flask import Flask, render_template, request
import csv
app = Flask(__name__)

FillPro = ['Id,','Name,,','Balance']
FieldProName = ['Id','Name','','Balance']
FieldTranName = ['Type','Balance','Time','Id','Amount','IdTran']
ID = ['58010866,','58011214,','58010860,','58011470,','58011148,']
NAME = [['neen,','ja,'],['eve,','ja,'],['boat,','ja,'],['ong,','ja,'],['bast,','jaja,']]
BALANCE = [1500,2300,14.1,13.6,655.3]
FillTran = ['Type,','Balance,','Time,','Id,','Amount,','IdTran']
kmitlID = 'KMITL'
Fee = 1
MoneyLimit = 5000

@app.route('/')
def KM_To_KM_main():
	return render_template('Transfer.html')

@app.route('/confirmTransfer',methods=['POST'])
def contransfer():
	kid = request.form['id']
	amount = request.form['amount']
	total = int(amount)+int(Fee)
	name = readNamePro(kid)

	return render_template('transfer2.html',kid=kid,amount=amount,fee=Fee,total=total,name=name)

@app.route('/suscessTransfer',methods=['POST'])
def sucTrans():
	balance = readDataPro('58010866')
	return render_template('transfer3.html')

def readNamePro(ID):
    with open('profile.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Id'] == ID:
                return row['Name']
def writeFillPro(profile):
    for subfill in FillPro:
        profile.write(subfill)
    profile.write('\n')
def writeFillTran(transaction):
    for subfill in FillTran:
        transaction.write(subfill)
    transaction.write('\n')
def writeDataTran(_type,balance,time,Id,amount,IdTran):
    line = []
    check = False
    with open('transaction.csv') as csvfile, open('tranfile.csv','w') as output:
        reader = csv.DictReader(csvfile)
        writer = csv.DictWriter(output,fieldnames=FieldName)
        writeFillTran(output)
        for row in reader:
            writer.writerow(row)
        #writer.writerow(row)
    #shutil.move('tranfile.csv','transaction.csv')
    """
    transaction.write(_type+',')
    transaction.write((str)(balance)+',')
    transaction.write(time+',')
    transaction.write(Id+',')
    transaction.write((str)(amount)+',')
    transaction.write(IdTran)
    """
def readDataPro(ID):
    count = 0
    start = False
    with open('profile.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Id'] == ID:
                return row['Balance']
def readTranID():
    with open('transaction.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        lastRow = 0
        for row in reader:
            lastRow = row['IdTran']
        lastRow = (int)(lastRow)
    print(lastRow)
    return lastRow
def checkMoneyLimit(amount):
    if amount + Fee <= MoneyLimit:
        return True
    return False
def checkMoneySent(idSent,amount):
    balance=readDataPro(idSent)
    balance=(float)(balance)
    if balance >= amount + Fee:
        return True
    return False
def checkID(ID):
    with open('profile.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for col in row.items():
                if col[0] == 'Id' and col[1] == ID:
                    return True
    return False
def checkMoneyReceive(idReceive,amount):
    balance = readDataPro(idReceive)
    balance = (float)(balance)
    if balance + amount <= MoneyLimit:
        return True
    return False
def updatePro(ID,amount):
    line = []
    check = False
    with open('profile.csv') as csvfile, open('outputfile.csv','w') as output:
        reader = csv.DictReader(csvfile)
        writer = csv.DictWriter(output,fieldnames=FieldName)
        writeFillPro(output)
        for row in reader:
            if row['Id'] == ID:
                writer.writerow({FieldName[0]:row['Id'],FieldName[1]:row['Name'],FieldName[2]:row[''],FieldName[3]:amount})
            else:
                writer.writerow(row)
    shutil.move('outputfile.csv','profile.csv')
def deductMoney(ID,amount):
    idtran = readTranID()
    balance = readDataPro(ID)
    balance = (float)(balance)
    balance -= amount
    #writeDataTran('Tranfer',balance,'12:12',ID,amount,idtran)
    updatePro(ID,balance)
    balance = balance - 1
    updatePro(ID,balance)
    return readDataPro(ID)
def addMoney(ID,amount):
    balance = readDataPro(ID)
    balance = (float)(balance)
    balance += amount
    updatePro(ID,balance)
    return readDataPro(ID)
    #print(line)
def addFee(ID):
    balance = readDataPro(ID)
    balance = (float)(balance)
    balance += 1
    updatePro(ID,balance)
    return readDataPro(ID)


if __name__ == "__main__" :
	app.run(host="0.0.0.0",debug=True)