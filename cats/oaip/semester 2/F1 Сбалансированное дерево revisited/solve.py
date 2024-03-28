def reading(name):
    with open(name, 'r') as f:
        return list(map(int, f.read().split()))


def writing(name, res):
    with open(name, 'w') as f:
        res = sorted(res)
        for value in res:
            if value != 0 and value != -1:
                f.write(str(value) + " ")


def solve():
    ht_size = 10 ** 6 + 1
    ht = [0] * ht_size

    def h(x):
        return (17 * x + 107) % ht_size

    def find(value, delete=False):
        hash_val = h(value)
        if ht[hash_val] == 0 or ht[hash_val] == value or ht[hash_val] == -1:
            if not delete:
                ht[hash_val] = value
            else:
                ht[hash_val] = -1
        else:
            for i in range(ht_size):
                index = (hash_val + i) % ht_size
                if ht[index] == 0:
                    if not delete:
                        ht[index] = value
                    else:
                        ht[index] = -1

    def ht_add(value):
        find(value)

    def ht_del(value):
        find(-value, True)

    numbers = reading("input.txt")

    for num in numbers:
        if num > 0:
            ht_add(num)
        elif num < 0:
            ht_del(num)
        else:
            break

    writing("output.txt", ht)


if __name__ == "__main__":
    solve()
