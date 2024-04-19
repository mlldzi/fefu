import re


def is_number(string):
    sub = re.match(r"^(-)?\d+(\.\d+)?$", string)
    if sub or (string[0] == '-' and sub):
        return True
    else:
        return False


def remove_spaces(expression):
    return re.sub(r"\s+", " ", expression)
