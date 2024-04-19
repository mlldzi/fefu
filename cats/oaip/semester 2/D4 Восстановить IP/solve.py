def isCorrect(string):
    if string[0] == '.' or string[-1] == '.':
        return False
    if '..' in string:
        return False

    for num in string.split('.'):
        if num[0] == '0' and len(num) != 1:
            return False
        if not (0 <= int(num) <= 255):
            return False
    return True


def permutations(parts, per, current, maxLength, isUsed):
    if len(current) == maxLength:
        per.append(current)
        return
    for i in range(len(parts)):
        if not isUsed[i]:
            isUsed[i] = True
            permutations(parts, per, current + parts[i], maxLength, isUsed)
            isUsed[i] = False


def main():
    with open('input.txt') as f:
        parts = []
        maxLength = 0
        for line in range(4):
            line = f.readline()
            temp = line.strip()
            maxLength += len(temp)
            parts.append(temp)

    used = [False] * len(parts)
    per = []
    result = set()

    permutations(parts, per, "", maxLength, used)

    for ip in per:
        if isCorrect(ip):
            result.add(ip)

    with open('output.txt', 'w') as f:
        for ip in sorted(result):
            f.write(ip + '\n')


if __name__ == '__main__':
    main()
