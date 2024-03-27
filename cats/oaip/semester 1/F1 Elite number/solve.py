def correct(num, index):
    num = list(str(num))
    f = "".join(num[0:index])
    s = str(int(num[index]) + 1)
    t = len(num[index + 1:])
    t *= "1"
    return f + s + t


def is_elite(num):
    sub = int(num)
    while sub > 0:
        last = sub % 10
        if last == 0:
            return False
        if num % last != 0:
            return False
        sub //= 10
    return True

def skip(num):
    number = list(str(num))
    flag_even = False
    flag_zero = False
    flag_five = False
    for i in range(len(number)):
        if number[i] == "0":
            flag_zero = True
        if number[i] in ("2", "4", "6", "8"):
            flag_even = True
        if number[i] == "5":
            flag_five = True
        if (flag_five and flag_even) or flag_zero:
            num = int(correct(num, i))
            break
    return num

with open("input.txt", "r") as inputfile, open("output.txt", "w") as out:
    n = int(inputfile.readlines()[0])
    while not is_elite(n):
        n = skip(n + 1)

    out.write(str(n))
