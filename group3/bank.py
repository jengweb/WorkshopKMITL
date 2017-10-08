import csv
import pandas as pd
class bank(): 
    def search(Database,data):
        for i in range(len(Database)):
            if data==Database[i][0]:
                return i
        return  0
    
    def sendtoBank(donateID,money):
        with open('BankDatabase.csv','r') as BankCsv:
            reader = csv.reader(BankCsv)
            customer = list(reader)
        index = bank.search(customer,donateID)
        amount = float(customer[index][1])
        if float(customer[index][2])>=float(money)+amount:
            return True
        else:
            return False
    
    def tranfered(donateID,money):
        with open('BankDatabase.csv','r') as BankCsv:
            reader = csv.reader(BankCsv)
            customer = list(reader)
        index = bank.search(customer,donateID)
        amount = float(customer[index][1]) + float(money)
        customer[index][1] = str(amount)
        df = pd.DataFrame(customer)
        df.to_csv("mylist.csv",index=False,header=False)