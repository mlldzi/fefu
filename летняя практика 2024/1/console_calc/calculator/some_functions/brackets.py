from calculator.math_functions.math_funcs import functions


def brackets_fix(expression):
    """
    Функция для убирания пробелов после и перед скобками в sin, log...
    также для убирания пробелов в скобах в сложных выражениях
    """

    if "( " in expression:
        expression = expression.replace("( ", "(")

    if " )" in expression:
        expression = expression.replace(" )", ")")
    if ' ,' in expression:
        expression = expression.replace(" ,", ",")

    for i in functions:
        if i in expression and i != '!':
            expression = expression.replace(f"{i} ", f"{i}")

        elif i == '!':
            expression = expression.replace(f" {i}", f"{i}")
    return expression
