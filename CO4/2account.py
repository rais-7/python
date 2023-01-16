class Account:
    def __init__(self,AccNumber,name,type,balance):
        self.AccNumber = AccNumber
        self.name = name
        self.type = type
        self.balance = balance
    def withdraw(self,amount):
        if(self.balance < amount):
            print ("insufficient balance")
            return
        self.balance -= amount
        return self.balance
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    def transfer(self,amount,Account):
        self.balance -= amount
        Account.balance += amount

    

acc1 = Account(5630,'arun','savings',2300)
acc2 = Account(7591,'abhi','current',1900)

acc1.withdraw(acc1.balance+50) 

acc2.deposit(30) 

acc1.transfer(600,acc2) 

print("propertise of "+ acc1.name , vars(acc1))
print("propertise of "+ acc2.name , vars(acc2))

