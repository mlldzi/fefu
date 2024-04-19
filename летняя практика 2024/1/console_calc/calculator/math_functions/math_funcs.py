from .basic import *
from .trigonometry import *
from calculator.some_functions.parent_classes import OneArg, MultiArgs


class Factorial(OneArg):
    """
    Факториал
    """

    def calculate(self):
        return math.factorial(self.a)


class Exp(OneArg):
    """
    Экспонента
    """

    def calculate(self):
        return math.exp(self.a)


class Log(OneArg):
    """
    Логарифм по произвольному основанию
    """

    def calculate(self):
        return math.log(self.a, 2)


class Lg(OneArg):
    """
    Десятичный логарифм
    """

    def calculate(self):
        return math.log10(self.a)


class Ln(OneArg):
    """
    Логарифм по основанию e
    """

    def calculate(self):
        return math.log(self.a, math.e)


class Sqrt(OneArg):
    """
    Квадратный корень числа
    """

    def calculate(self):
        return math.sqrt(self.a)


class Gcd(MultiArgs):
    """
    Наибольший общий делитель
    """

    def calculate(self):
        return math.gcd(*self.args)


class Lcm(MultiArgs):
    """
    Наименьшее общее кратное
    """

    def calculate(self):
        return math.lcm(*self.args)


operators = {Add: '+', Subtract: '-', Multiply: '*', Divide: '/', Power: '^', Mod: 'mod или %', Log: 'log', Lg: 'lg',
             Ln: 'ln', Sqrt: 'sqrt', Sin: 'sin', Cos: 'cos', Tan: 'tan или tg', Factorial: '!', Gcd: 'gcd', Lcm: 'lcm',
             Exp: 'exp'}
functions = ['sqrt', 'sin', 'cos', 'tan', 'tg', 'log', 'lg', 'ln', '!', 'gcd', 'lcm', 'нод', 'нок', 'exp']
