from .fix_string import fix_string_for_parse_input
from calculator.math_functions.math_funcs import Gcd, Lcm
from calculator.some_functions.regulars import is_number
from calculator.some_functions.work_with_num import *


class Parser:
    OPERATOR_PRIORITY = {
        '+': 1, '-': 1,
        '*': 2, '/': 2,
        '^': 3, 'mod': 3, '%': 3, '!': 3,
        'sqrt': 4, 'sin': 4, 'cos': 4, 'tan': 4, 'tg': 4, 'lg': 4, 'ln': 4,
        'gcd': 5, 'lcm': 5, 'exp': 5, 'log': 5
    }

    SPECIAL_FUNCTIONS = {'gcd': Gcd, 'нод': Gcd, 'lcm': Lcm, 'нок': Lcm}

    def __init__(self, expression):
        self.expression = expression
        self.elements = fix_string_for_parse_input(expression).split()
        self.operator_stack = []
        self.postfix_notation = []

        self.spec_func = None
        self.nums_for_spec_functions = []

        self.exp_flag = None
        self.num_for_exp = []

        self.log_flag = None
        self.nums_for_log = []

    def parse_input(self):
        for element in self.elements:
            self.parse_element(element)

        while self.operator_stack:
            if self.operator_stack[-1] == '(':
                raise ValueError("Неправильное расположение скобок в выражении")
            self.postfix_notation.append(self.operator_stack.pop())
        return self.postfix_notation

    def parse_element(self, element):
        if element in self.SPECIAL_FUNCTIONS or self.spec_func is not None:
            self.parse_special_function(element)
        elif element == 'exp' or self.exp_flag is not None:
            self.parse_exp(element)
        elif element == 'log' or self.log_flag is not None:
            self.parse_log(element)
        elif is_number(element):
            push_to_stack(element, self.postfix_notation)
        elif element in self.OPERATOR_PRIORITY:
            self.parse_operator(element)
        elif element in ['pi', 'p', '-pi', '-p']:
            check_for_pi(element, self.postfix_notation)
        elif element in ['e', '-e']:
            check_for_e(element, self.postfix_notation)
        elif element == '(':
            self.operator_stack.append(element)
        elif element == ')':
            self.parse_closing()
        else:
            raise ValueError("Некорректный символ")

    def parse_special_function(self, element):
        if self.spec_func is None:
            self.spec_func = element
        if element == ',':
            return
        self.nums_for_spec_functions.append(element)
        if element == ")":
            self.spec_func, self.nums_for_spec_functions = evaluate_special_function(
                self.SPECIAL_FUNCTIONS, self.spec_func, self.nums_for_spec_functions, self.postfix_notation)

    def parse_exp(self, element):
        if self.exp_flag is None:
            self.exp_flag = True
        self.num_for_exp.append(element)
        if element == ")":
            self.num_for_exp = evaluate_exp(self.num_for_exp, self.postfix_notation)
            self.exp_flag = None

    def parse_log(self, element):
        if self.log_flag is None:
            self.log_flag = True
        if element == ",":
            return
        self.nums_for_log.append(element)
        if element == ")":
            self.nums_for_log = evaluate_log(self.nums_for_log, self.postfix_notation)
            self.log_flag = None

    def parse_operator(self, element):
        while self.operator_stack and self.operator_stack[-1] != '(' and self.OPERATOR_PRIORITY.get(
                self.operator_stack[-1], 0) >= self.OPERATOR_PRIORITY[element]:
            self.postfix_notation.append(self.operator_stack.pop())
        self.operator_stack.append(element)

    def parse_closing(self):
        while self.operator_stack and self.operator_stack[-1] != '(':
            self.postfix_notation.append(self.operator_stack.pop())
        if self.operator_stack and self.operator_stack[-1] == '(':
            self.operator_stack.pop()
        else:
            raise ValueError("Неправильное расположение скобок")
