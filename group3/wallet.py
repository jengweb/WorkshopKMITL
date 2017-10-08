import csv

class wallet():

    def serchWallet(database,data):
        for i in range(len(database)):
            if data==database[i][0]:
                return i
        return 0

    def isEnought(acountID,money):
        with open('Balance.csv', 'r') as BalanceCsv:
            reader = csv.reader(BalanceCsv)
            customer = list(reader)
        index = wallet.serchWallet(customer,acountID)
        if float(customer[index][2])>=float(money):
            return True
        else:
            return False
