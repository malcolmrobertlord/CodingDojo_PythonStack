class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount # the specific user's account increases by the amount of the value received
    #adding the withdrawal method
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    #adding display balance method
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
    #adding transfer money method
    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount

jon = User("Jon Snow", "know@nothing.com")
monty = User("Monty Python", "monty@python.com")
darth = User("Darth Vader", "darthvader@evil.com")

jon.make_deposit(200)
jon.make_deposit(100)
jon.make_withdrawal(50)
jon.display_user_balance()

monty.make_deposit(400)
monty.make_deposit(200)
monty.make_withdrawal(100)
monty.make_withdrawal(200)
monty.display_user_balance()

darth.make_deposit(1000)
darth.make_withdrawal(100)
darth.make_withdrawal(50)
darth.make_withdrawal(50)
darth.display_user_balance()

jon.transfer_money(darth,200)
jon.display_user_balance()
darth.display_user_balance()