class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount # the specific user's account increases by the amount of the value received
        return self
    #adding the withdrawal method
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    #adding display balance method
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self
    #adding transfer money method
    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

jon = User("Jon Snow", "know@nothing.com")
monty = User("Monty Python", "monty@python.com")
darth = User("Darth Vader", "darthvader@evil.com")

jon.make_deposit(200).make_deposit(100).make_withdrawal(50).display_user_balance()

monty.make_deposit(400).make_deposit(200).make_withdrawal(100).make_withdrawal(200).display_user_balance()

darth.make_deposit(1000).make_withdrawal(100).make_withdrawal(50).make_withdrawal(50).display_user_balance()

jon.transfer_money(darth,200).display_user_balance()
darth.display_user_balance()