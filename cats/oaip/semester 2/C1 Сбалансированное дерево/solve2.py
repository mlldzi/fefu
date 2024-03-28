arr = set()
with open("input.txt", "r") as fin, open("output.txt", "w") as fout:
    nums = map(int, fin.readline().strip().split(' '))
    for num in nums:
        if num > 0:
            arr.add(num)
        if num < 0 and abs(num) in arr:
            arr.remove(abs(num))
        if num == 0:
            for i in arr:
                fout.write(str(i) + ' ')
            break