from .parser import Parser
from .postfix import evaluate_postfix
from .exceptions import check_for_command, check_for_exit
from calculator.some_functions.work_with_history import logging_history


class Calculator:

    def start(self):
        while True:
            user_input = input("Введите выражение: ")

            if check_for_exit(user_input):
                break
            if check_for_command(user_input):
                self.start()
                break

            try:
                expression = Parser(user_input).parse_input()
                result = evaluate_postfix(expression)
                logging_history(user_input, result)
                print(result)

            except ValueError as error:
                print(error)
