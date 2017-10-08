import csv
import os
import sys
balancePoint=0
accountID=0
accountData=[]
promotionData=[]
import checkUse
def getBalancePointAndPromotion(accountID) :
    accountID='C:/Users/kaogi/Desktop/mini/accountDB/'+accountID+ ".csv"
    with open(accountID) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader :
            accountData.append(row)
    with open('C:/Users/kaogi/Desktop/mini/promotionDB/promotion.csv', encoding="utf8") as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader :
            promotionData.append(row)        
    balancePoint=accountData[3][0]
    name=accountData[1][0]
    return int(balancePoint),name,promotionData,accountData
