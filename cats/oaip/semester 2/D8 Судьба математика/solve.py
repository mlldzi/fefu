MAX = 1000000

#
#
# TL SOLVE
#
class Condition:
    def __init__(self, l, r, op):
        self.l = l
        self.r = r
        self.op = op


def to_cond(l):
    operand = l[1:-1]
    normal = {
        '=': 1,
        '>': 2,
        '<': 3,
        '<>': 4,
        '>=': 5,
        '<=': 6
    }
    html = {
        '&gt;': 2,
        '&lt;': 3,
        '&lt;&gt;': 4,
        '&gt;=': 5,
        '&lt;=': 6
    }
    try:
        temp = normal[operand]
    except:
        temp = html[operand]
    return Condition(int(l[0]), int(l[-1]), temp)


def is_right(j):
    global Conditions, Number
    op = Conditions[j].op
    l = Conditions[j].l
    r = Conditions[j].r
    if op == 1:
        return Number[l] == Number[r]
    elif op == 2:
        return Number[l] > Number[r]
    elif op == 3:
        return Number[l] < Number[r]
    elif op == 4:
        return Number[l] != Number[r]
    elif op == 5:
        return Number[l] >= Number[r]
    elif op == 6:
        return Number[l] <= Number[r]


def increment():
    global Number
    k = 6
    Number[k] += 1
    while Number[k] == 10:
        Number[k] = 0
        k -= 1
        Number[k] += 1


def main():
    global Conditions, Number
    with open('input.txt', 'r') as fin, open('output.txt', 'w') as fout:
        Conditions = [to_cond(line.strip()) for line in fin.readlines()]
        count = 0
        Number = [0] * 7
        for i in range(MAX):
            count += 1
            for j in range(len(Conditions)):
                if not is_right(j):
                    count -= 1
                    break
            increment()
        fout.write(str(count))


if __name__ == '__main__':
    main()
