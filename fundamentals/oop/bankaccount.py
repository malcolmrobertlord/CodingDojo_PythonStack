class BankAccount:
    all_accounts=[]
    def __init__(self, int_rate=.01, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    
    #class method to print all the account info
    @classmethod
    def print_all_accounts(cls):
        print("Here are all the account balances:")
        for account in cls.all_accounts:
            print(f"Balance: {account.balance}")
    
    # methods
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Insufficient funds: charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            return self

#creating accounts
account1 = BankAccount()
account2 = BankAccount()

#changing to accounts
account1.deposit(200).deposit(100).deposit(100).withdraw(200).yield_interest().display_account_info()
account2.deposit(300).deposit(300).withdraw(100).withdraw(80).withdraw(20).withdraw(100).yield_interest().display_account_info()

#class method call
BankAccount.print_all_accounts()