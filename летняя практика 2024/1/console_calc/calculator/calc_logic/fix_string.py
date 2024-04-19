from calculator.some_functions.regulars import remove_spaces


def fix_string_for_parse_input(expression):
    """
    Функция для добавления пробелов в выражение для корректного парсинга
    """
    expression_with_spaces = ""
    is_prev_char_digit = False
    for char in expression:
        if char.isdigit() or char.isalpha() or char == '.':
            expression_with_spaces += char
            is_prev_char_digit = True
        elif char == '-' and (not expression_with_spaces or expression_with_spaces[-1] in [' ', '(']):
            expression_with_spaces += char
            is_prev_char_digit = False
        else:
            if is_prev_char_digit:
                expression_with_spaces += " "
            expression_with_spaces += " " + char + " "
            is_prev_char_digit = False

    expression_with_spaces = remove_spaces(expression_with_spaces)

    result = ""
    for element in expression_with_spaces.split():  # для перевода всех функций в нижний регистр
        result = result + ' ' + str(element).lower()

    result = result.strip()
    return result
