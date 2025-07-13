def add(a, b):
    return a + b
def square(x):
    return x * x
def multiply(a, b):
    return a * b

#UNIT TEST
def calculate_expression(x, y):
    return add(square(x), multiply(y, 2))

#REGRESSION TEST
def calculate_expression2(x, y, z=0):
    return add(square(x), multiply(y, 2))

def test_calculate_expression():
    assert calculate_expression(2, 3) == 10
    assert calculate_expression(0, 5) == 10



print("All integration tests passed!")

test_calculate_expression()