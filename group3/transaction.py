import csv
import pandas as pd
from bank import bank
from wallet import wallet
import time

class transaction():
    def createTransaction(accountID,donateID,money):
        with open('balance.csv','r') as BankCsv:
            reader = csv.reader(BankCsv)
            customer = list(reader)
        index = wallet.serchWallet(customer,accountID)
        date = time.strftime("%d/%m/%Y")
        print(customer)
        newdata=[customer[index][0],[customer[index][1]],money,donateID,0,date,"Waiting"]
        with open('Transaction.csv','r') as BankCsv:
            reader = csv.reader(BankCsv)
            tranData = list(reader)
        tranData.append(newdata)
        print(tranData)
        df = pd.DataFrame(tranData)
        df.to_csv("newTran.csv",index=False,header=False)

transaction.createTransaction("58010781","1001","50.00")