class TwoArgs:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.result = self.calculate()

    def __repr__(self):
        return str(self.result)

    def calculate(self):
        pass


class OneArg:
    def __init__(self, a):
        self.a = a
        self.result = self.calculate()

    def __repr__(self):
        return str(self.result)

    def calculate(self):
        pass


class MultiArgs:
    def __init__(self, *args):
        self.args = args
        self.result = self.calculate()

    def __repr__(self):
        return str(self.result)

    def calculate(self):
        pass
