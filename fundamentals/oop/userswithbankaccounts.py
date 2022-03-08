class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account.deposit(amount) # the specific user's account increases by the amount of the value received
        return self
    #adding the withdrawal method
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    #adding display balance method
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.balance}")
        return self
    #adding transfer money method
    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self
    #adding bank account method
    def add_account(self,user):
        user.account = BankAccount()

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

jon = User("Jon Snow", "know@nothing.com")
monty = User("Monty Python", "monty@python.com")
darth = User("Darth Vader", "darthvader@evil.com")



jon.make_deposit(200).make_deposit(100).make_withdrawal(50).display_user_balance()