words, sub = [], []
max_difts = -1


def is_vowel(a):
    return a in ['a', 'e', 'i', 'o', 'u', 'y']


with open('input.txt', 'r') as f:
    n = int(f.readline())
    for _ in range(n):
        word = f.readline().strip()
        sub.append(word)

for word in sub:
    dipht_cnt = 0
    flag = False
    if len(word) < 2:
        flag = True
    if len(word) == 2 and is_vowel(word[0]) and is_vowel(word[1]):
        dipht_cnt = 1
        flag = True
    for j in range(len(word)):
        if flag:
            break
        if not is_vowel(word[j]):
            if j + 2 < len(word):
                if is_vowel(word[j + 1]) and is_vowel(word[j + 2]) and j + 3 == len(word):
                    dipht_cnt += 1
                    break
                elif is_vowel(word[j + 1]) and is_vowel(word[j + 2]) and not is_vowel(word[j + 3]):
                    dipht_cnt += 1
                    j += 2
        elif j == 0 and is_vowel(word[j]) and is_vowel(word[j + 1]) and not is_vowel(word[j + 2]):
            dipht_cnt += 1
    words.append((word, dipht_cnt))
    if max_difts < dipht_cnt:
        max_difts = dipht_cnt

with open('output.txt', 'w') as f:
    for i in range(len(words)):
        if words[i][1] == max_difts:
            f.write(words[i][0] + '\n')
