class Calculator:
    def multiply(self, x, y):
        return x * y

    def division(self, x, y):
        if y ==0:
            raise ZeroDivisionError
        return x / y

    def subtraction(self, x, y):
        return x - y

    def adding(self, x, y):
       return x + y
