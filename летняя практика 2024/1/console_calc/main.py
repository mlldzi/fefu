from sys import path

path.append(r"..\\calculator")
from calculator.calc_logic.calc import Calculator


def main():
    calc = Calculator()
    calc.start()


if __name__ == "__main__":
    main()
