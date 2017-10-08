import csv
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

def generatePromotionCode(studentID,promotionID):
    BackSubstringStudentID = studentID[4:] #Extract Substring from Student ID Example 5801|1234 = 1234
    PromotionCode = BackSubstringStudentID[::-1] + studentID[:4] + promotionID #[::-1] is Reversing String
    return PromotionCode

def getPromotionDetail(ChosenPromotionID):
    promotionData=[]
    with open('C:/Users/kaogi/Desktop/mini/promotionDB/promotion.csv', encoding="utf8") as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader :
            promotionData.append(row)
    for i in range(len(promotionData)):
        if (promotionData[i][0]==ChosenPromotionID):
            promotionDetail = promotionData[i][4]
    return promotionDetail

def isEnoughtoPay(findID ,currentBalance):
    index = 999
    with open('C:/Users/kaogi/Desktop/mini/promotionDB/promotion.csv', encoding="utf8") as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            promotionData.append(row)
    for i in range(0,len(promotionData)):
        if(promotionData[i] == findID):
            index = i
    if index != 999:
        if(int(promotionData[index]) < currentBalance):
            print ('okay')
            return True
        else:
            print('not enough')
            return False
    else:
        print('cant find')
        return False

def decreasePoint(balancePoint,usePoint):
#Balance Point from DB Ex.58010300 has 600 Points
#usePoint from PromotionDB Ex.TrueCoffee use 300 Points
    remainPoint = balancePoint - usePoint
    return remainPoint

def isUsed(accountID,promotionID):
    accountDATA = 'C:/Users/kaogi/Desktop/mini/accountDB/' + accountID + ".csv"
    with open(accountID) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            accountDATA.append(row)
    wasRedeemed = False
    for i in range(0,len(accountDATA[2])) :
        if(accountDATA[2][i] == promotionID):
            wasRedeemed = True
    for k in range(0,len(accountDATA[4])) :
        if(accountDATA[4][k] == promotionID):
            wasRedeemed = True
    return wasRedeemed


