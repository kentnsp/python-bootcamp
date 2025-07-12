class Bank_account:
    def __init__(self, balance):
        self._balance = balance


    def deposit(self, amount):
        self._balance += amount
        print(self._balance)

    def withdraw(self, amount):
        self._balance -= amount
        print(self._balance)

account1 = Bank_account(0)
account1.deposit(500)
account1.withdraw(200)

