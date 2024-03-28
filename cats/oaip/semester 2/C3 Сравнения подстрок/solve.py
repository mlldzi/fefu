def hash(s):
    p = 31
    m = 10 ** 9 + 9
    res = 0
    p_pow = 1
    for char in s:
        res = (res + (ord(char) - ord('a') + 1) * p_pow) % m
        p_pow = (p_pow * p) % m
    return res


def comp_hashes(s):
    n = len(s)
    p = 31
    m = 10 ** 9 + 9
    p_pow = [1]
    hashes = [0]
    for i in range(1, n + 1):
        p_pow.append((p_pow[-1] * p) % m)
        hashes.append((hashes[-1] + (ord(s[i - 1]) - ord('a') + 1) * p_pow[i]) % m)
    return hashes, p_pow


def substring_hash(hashes, p_pow, a, b):
    m = 10 ** 9 + 9
    return (hashes[b] - hashes[a - 1] + m) % m * p_pow[len(hashes) - a] % m


s = input().strip()
n = len(s)
hashes, p_pow = comp_hashes(s)

m = int(input())
for _ in range(m):
    a, b, c, d = map(int, input().split())
    hash1 = substring_hash(hashes, p_pow, a, b)
    hash2 = substring_hash(hashes, p_pow, c, d)

    if hash1 == hash2:
        print("Yes")
    else:
        print("No")
