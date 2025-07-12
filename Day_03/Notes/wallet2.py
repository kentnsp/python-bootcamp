class Wallet:
    def __init__(self, initial_amount = 0):
        self._amount = initial_amount

    @property
    def amount(self):
        return  self._amount

    @amount.setter
    def amount(self, new_value):
        self._amount = new_value

food_wallet = Wallet(250)
food_wallet.amount += 1_000

print("Food budget:", food_wallet.amount)