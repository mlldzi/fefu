from calculator.math_functions.math_funcs import operators
from calculator.some_functions.decorators import decorator_sub
from calculator.some_functions.work_with_history import read_history


@decorator_sub('*')
def print_info():
    print("Возможные команды:")
    for i in operators:
        print(f'{operators[i]} - {i.__doc__.strip()}')


@decorator_sub('-')
def print_history(length=None):
    if length is None:
        length = 9
    print(read_history(length))


def check_for_command(user_input):
    if user_input == "":
        return True

    help_phrases = ["help", "помощь", "h"]
    if user_input in help_phrases:
        print_info()
        return True

    check_for_num = user_input.split()
    history_phrases = ["history", "история", "историю", "his"]
    if check_for_num[0] in history_phrases and len(check_for_num) == 2 and check_for_num[1].isdigit():
        print_history(int(check_for_num[1]))
        return True
    elif check_for_num[0] in history_phrases and len(check_for_num) == 1:
        print_history()
        return True


def check_for_exit(user_input):
    phrases = ["goodbye", "exit", "quit", "выход", "стоп", "stop", "bye"]
    if user_input.lower() in phrases:
        return True
