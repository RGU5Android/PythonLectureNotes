#!/usr/bin/python

def print_line():
    print "-----------------------------------------------------------------------------------------------------------------------------"

class BankAccount:
    account_number = 2305

    def __init__(self, name, balance):
        print "INIT of base class"
        self.name = name
        self.__ac_number = BankAccount.account_number
        BankAccount.account_number += 1
        self.balance = balance

    def withdraw(self, amount):
        print "Withdraw amount: " +str(amount)
        if((self.balance - amount) > 0):
            self.balance = self.balance - amount
        else:
            print "Amount is greater than available balance"
        print "Transaction Completed."

    def deposite(self, amount):
        print "Deposite amount: " +str(amount)
        self.balance = self.balance + amount
        print "Transaction Completed"

    def __str__(self):
        # return "Name: " +self.name +" || Account Number: " +str(self.__ac_number) +" || Balance: " +str(self.balance)
        return self.__print_account_details()

    def __print_account_details(self):
        return "Name: " +self.name +" || Account Number: " +str(self.__ac_number) +" || Balance: " +str(self.balance)

class CurrentAccount(BankAccount):
    def __init__(self, name1, balance1):
        print "INIT of derived class"
        super(CurrentAccount, self).__init__(name1, balance1)

b1 = BankAccount("Rahul", 1000)
print b1
print_line()
b1.deposite(100)
b1.withdraw(5)
print b1
print_line()

b2 = BankAccount("Zakariya", 1000000)
print b2
print_line()
b2.deposite(1)
b2.withdraw(11111111111111111)
print b2
print_line()

b3 = BankAccount("Abhishek", 1000)
print b3
print_line()
b3.deposite(111111111111111111111)
print b3
print_line()


b4 = BankAccount("Yogesh", 1000000)
print b4
print_line()
print_line()
print_line()

print b1.__dict__
print b2.__dict__
print b3.__dict__
print b4.__dict__

print b1._BankAccount__print_account_details()
print b2._BankAccount__print_account_details()
print b3._BankAccount__print_account_details()
print b4._BankAccount__print_account_details()

c1 = CurrentAccount("GoDzPlaY", 5000)
print c1.__dict__
