#create account class with 2 attributes- balance &  account no
#create a method for debit, credit & printing the balance

class Account:
    def __init__(self,account_no,balance):
        self.acc=account_no
        self.bal=balance


    #debit money
    def deb(self,amount):
        if amount<=0:
            print("must be positive")
        else:
            self.bal = self.bal - amount
            print("money debited, available balance: ", self.bal)

    def cred(self,amount):
        if amount<=0:
            print("must be positive")
        else:
            self.bal = self.bal + amount
            print("money credited, available balance: ", self.bal)


acc1=Account(12345,12000)
print("Account no:",acc1.acc,"balance is",acc1.bal)
acc1.deb(1000)
acc1.cred(40000)
