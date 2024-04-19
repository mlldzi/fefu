import math
from calculator.some_functions.parent_classes import OneArg


class Sin(OneArg):
    """
    Синус
    """

    def calculate(self):
        return round(math.sin(self.a), 15)


class Cos(OneArg):
    """
    Косинус
    """

    def calculate(self):
        return round(math.cos(self.a), 15)


class Tan(OneArg):
    """
    Тангенс
    """

    def calculate(self):
        return Cos(self.a).calculate() / Sin(self.a).calculate()


class Tg(Tan):
    pass
