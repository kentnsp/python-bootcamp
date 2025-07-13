def square(x):
    return x * x

class TestSquarePositive:
    def test_square_positive_1(self):
        assert square(2) == 4
    def test_square_positive_2(self):
        assert square(3) == 9

class TestSquareSpecialCase:
    def test_square_negative(self):
        assert square(-3) == 9
    def test_square_zero(self):
        assert square(0) == 0

