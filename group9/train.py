import csv


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

findAvailableBalance("58010000")
