import csv


class Table:
    def __init__(self, dbname):
        self.tablename = dbname + '.csv'
        open(dbname + '.csv', 'w+')

    def createField(self, text):
        with open(self.tablename,'w') as file:
            cr = csv.writer(file,delimiter=",",lineterminator="\n")
            cr.writerow(text)

    def insert(self, text):
        with open(self.tablename,'a') as file:
            cr = csv.writer(file,delimiter=",",lineterminator="\n")
            cr.writerow(text)

    def queryAll(self):
        result = []
        with open(self.tablename, "r") as file:
            cr = csv.reader(file, delimiter=' ', quotechar='|')
            for i, row in enumerate(cr):
                if i > 0:
                    result.append(row)
        return result

profile = 'name, id, password, balance'
transaction = 'date, transaction, type, amount remain'

transaction = Table('transaction') # create database name 'transaction'
transaction.createField(['date','transaction','type', 'amount', 'remain'])
transaction.insert(['11/11/2511','111','outcome', '1111', '1234'])
transaction.insert(['22/22/2522','222', 'income','2222', '1234'])

profile = Table('profile')
profile.createField(['id', 'name', 'balance', 'password'])
profile.insert(['58011420', 'micky mouse', '2300', '1234'])
profile.insert(['zzzz', 'zzzz', '234234', '1234'])


