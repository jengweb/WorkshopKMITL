import pandas as pd
import csv
from wallet import wallet
from bank import bank
#def acceptance()
class acceptance():
    def acceptance(donateID,acountID,money):
        benought = wallet.isEnought(acountID,money)
        with open('EventDonate.csv','r') as BankCsv:
            reader = csv.reader(BankCsv)
            customer = list(reader)
        bankID = ""
        for index in range(len(customer)):
            if donateID == customer[index][0]:
                bankID = customer[index][4]
                break
        bgoal = acceptance.isOverGoal(bankID,money)
        if benought and bgoal:
            return True
        else:
            return False
    
    def isOverGoal(acountID,money):
        return bank.sendtoBank(acountID,money)
acceptance.acceptance("1000","58010781","50")
   
    
    