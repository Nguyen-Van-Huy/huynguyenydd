class Bank:
    Account_type = "Savings"
    location = "Guntur"
    def __init__(self, name, Account_Number, balance):
        self.name = name
        self.Account_Number = Account_Number
        self.balance = balance
        self.Account_type = Bank.Account_type
        self.location = Bank.locaton

    def __repr__(self):
        print("Wecome to the SBI ATM Machine ")
        print("------------------------------")
        account_pin = int(input("Please enter your pin number "))
        if(account_pin==123):
            Account(self)
        else:
            print("Pin Incorrect. Please try again")
            Eror(self)
        return ' '.join([self.name,self.Account_Number])
def Error(self):

    account_pin = int(input("Please enter your pin number "))
    if(account_pin==123):
            Account(self)
        else:
            print("Pin Incorrect. Please try again")
            Eror(self)
def Account(self):
    print("Your Card Number Is: XXXX XXXX XXXX 1337")
    print("Would you like to deposit/withdraw/Check Balance?")
    print("""
1)         Balance
2)         Withdaw
3)         Deposit
4)         Quit
""")
    option=int(input("Please enter your choice:"))
    if(option==1)
        Balance(self)
    elif(option==2)
        Withdaw(self)
    elif(option==3)
        Deposit(self)
    elif(option==4)
        exit()
    
def Balance(self):
    print("Balance:",selfbalance)
    Account(self)
def Withdraw(self):
    w=int(input("Please Enter Desired amount: "))
    if(self.balance>0 and self.balance>=w):
        self.balance=self.balance-w
        print("Your transaction is successfull")
        print("Your Balance:",self.balance)
        
        print(" ")
    else:
        print("Your transaction is cancelled due to")
        print("Amount is not sufficient in your account")
    Account(self)
def Deposit(self):
    d=int(input("Please Enter Desired amount:))
    self.balance=self.balance+d
    print("Your transaction is successfull")
    print("Balance:",self.balance)
    Account(self)
def Exit():
    print("Exit")
t1=Bank('mahesh', 1453210145,5000)

print(t1)
    












                
