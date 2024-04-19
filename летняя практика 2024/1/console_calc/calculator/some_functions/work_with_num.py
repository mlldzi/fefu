import math


def push_to_stack(element, stack):
    """
    Функция для добавления в массив(стек)
    """
    stack.append(to_num(element))


def to_num(element):
    try:
        return int(element)
    except:
        try:
            return float(element)
        except:
            pass


def check_for_pi(element, stack):
    if element in ['pi', 'p']:
        stack.append(math.pi)
    else:
        stack.append(-math.pi)


def check_for_e(element, stack):
    if element == 'e':
        stack.append(math.e)
    else:
        stack.append(-math.e)


def evaluate_special_function(functions, spec_func, nums_for_spec_functions, postfix_notation):
    """
    Функция для обработки НОД и НОК
    """
    nums = []
    for elem in nums_for_spec_functions[2:-1]:
        push_to_stack(elem, nums)

    spec_func_to_eval = functions[spec_func]
    postfix_notation.append(spec_func_to_eval(*nums))

    spec_func = None
    nums_for_spec_functions = []

    return spec_func, nums_for_spec_functions


def evaluate_exp(num_for_exp, postfix_notation):
    """
    Функция для обработки экспоненты
    """
    num_for_exp = to_num(num_for_exp[2])
    postfix_notation.append(math.exp(num_for_exp))
    num_for_exp = []
    return num_for_exp


def evaluate_log(nums_for_log, postfix_notation):
    """
    Функция для обработки логарифма, по умолчанию 2
    """
    if len(nums_for_log) == 5:
        num = to_num(nums_for_log[2])
        base = to_num(nums_for_log[3])
        result = math.log(num, base)
    else:
        num = to_num(nums_for_log[2])
        result = math.log(num, 2)

    postfix_notation.append(result)
    nums_for_log = []
    return nums_for_log
