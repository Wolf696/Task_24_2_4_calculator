import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding(self):
        assert self.calc.adding(self, 5, 6) == 11

    def test_subtraction(self):
        assert self.calc.subtraction(self, 3, 1) == 2

    def test_division(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_multiply(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def teardown(self):
        print('Tearing down')
