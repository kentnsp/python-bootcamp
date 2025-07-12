class NotANumber(ValueError):
    pass

class NotPositive(ValueError):
    pass

class NotWithinRange(ValueError):
    pass

user_input = input("Enter a positive number [1,100]: ")

if not user_input.isnumeric() and not user_input[1:].isnumeric():
    raise NotANumber("Not a number")

number = int(user_input)
if number < 0:
    raise NotPositive("Not positive")

if not (1 <= number <= 100):
    raise NotWithinRange("Not within range")