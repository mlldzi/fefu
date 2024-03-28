with open('input.txt') as fi:
    n = int(fi.readline())
    a = list(map(int, fi.readline().split()))
    m = int(fi.readline())
    b = list(map(int, fi.readline().split()))


def f(a, b):
    for i in range(n - m + 1):
        if all(a[i + j] - a[i] == b[j] for j in range(m)):
            return i + 1
    return -1


with open('output.txt', 'w') as fo:
    fo.write(str(f(a, b)))
