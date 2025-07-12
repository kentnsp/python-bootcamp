class Payment:
    def __init__(self, amount):
        self.amount = amount

    def valid(self):
        return self.amount >0


class Coupon(Payment):
    def __init__(self, amount, expired):
        super().__init__(amount)
        self.expired = expired

    def valid(self):
        return super().valid() and not self.expired


class CardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = str(card_number)

    def valid(self):
        return super().valid() and len(self.card_number) == 16


class OnlinePayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email

    def valid(self):
        return super().valid() and self.email.endswith("@gmail.com")


online_payment = OnlinePayment(5000,"ken@gmail.com")
print(online_payment.valid())

card_payment= CardPayment(1000,1234567890)
print(card_payment.valid())

coupon = Coupon(5000, False)
print(coupon.valid())

