from acceptance import acceptance
def donate(donateNID,accoutID,money):
    if acceptance.acceptance(donateNID,accoutID,money):
        print("Can Donate")
        return True
        #Tranfer
    else:
        print("Cannot Donate")
        return False
donate("1000","58010781","50.00")
