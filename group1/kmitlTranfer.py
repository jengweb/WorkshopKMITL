import shutil
import csv
FillPro = ['Id,','Name,,','Balance']
FieldProName = ['Id','Name','','Balance']
FieldTranName = ['Type','Balance','Time','Id','Amount','IdTran']
kmitlID = 'KMITL'
Fee = 1
MoneyLimit = 5000
def writeFillPro(profile):
    for subfill in FillPro:
        profile.write(subfill)
    profile.write('\n')

def readNamePro(ID):
    with open('profile.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Id'] == ID:
                return row['Name']
                
def readDataPro(ID):
    with open('profile.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Id'] == ID:
                return row['Balance']
            
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
    balance = readDataPro(ID)
    balance = (float)(balance)
    balance -= amount
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

def addFee(ID):
    balance = readDataPro(ID)
    balance = (float)(balance)
    balance += 1
    updatePro(ID,balance)
    return readDataPro(ID)

idSent = input("Input sent ID ")
idReceive = input("Input receive ID :")
nameSent = readNamePro(idSent)
nameReceive = readNamePro(idReceive)
amountTranfer = input("Input Amount ")
amountTranfer = (float)(amountTranfer)
if checkID(idSent):
    if checkMoneyLimit(amountTranfer):
        if checkMoneySent(idSent,amountTranfer):
            if checkID(idReceive):
                if checkMoneyReceive(idReceive,amountTranfer):
                    print(nameSent)
                    print(nameReceive)
                    print("senderBalance = ",deductMoney(idSent,amountTranfer))
                    print("recieverBalance = ",addMoney(idReceive,amountTranfer))
                    print("kmitlBalance = ",addFee(kmitlID))
                else:
                    print("not")
            else:
                print("Wrong IDnumber")
        else:
            print("Not enough Money")
    else:
        print("Can't tranfer more than 5000 bath")
else:
    print("Wrong IDnumber")


