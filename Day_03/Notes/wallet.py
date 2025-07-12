class Wallet:
    def __init__(self, initial_amount = 0):
        self.amount = initial_amount

food_wallet = Wallet(250)
food_wallet.amount += 1_000

print("Food budget:", food_wallet.amount)
