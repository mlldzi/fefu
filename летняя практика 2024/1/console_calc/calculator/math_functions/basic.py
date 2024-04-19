from calculator.some_functions.parent_classes import TwoArgs

class Add(TwoArgs):
    """
    Сложение
    """

    def calculate(self):
        return self.a + self.b


class Subtract(TwoArgs):
    """
    Вычитание
    """

    def calculate(self):
        return self.a - self.b


class Multiply(TwoArgs):
    """
    Умножение
    """

    def calculate(self):
        return self.a * self.b


class Divide(TwoArgs):
    """
    Деление
    """

    def calculate(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return "На ноль делить нельзя"


class Power(TwoArgs):
    """
    Возведение числа в степень
    """

    def calculate(self):
        return self.a ** self.b


class Mod(TwoArgs):
    """
    Остаток от деления
    """

    def calculate(self):
        return self.a % self.b
