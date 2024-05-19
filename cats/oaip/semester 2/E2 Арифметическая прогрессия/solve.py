def reading():
    with open("input.txt", "r") as input_file:
        sub = [i.strip() for i in input_file.readlines()]
        to_return = []
        for i in sub:
            for elem in i.split():
                to_return.append(int(elem))
        return to_return


def writing(ans, ans_arr):
    with open("output.txt", "w") as output_file:
        output_file.write(str(ans) + "\n")
        output_file.write(" ".join(str(x) for x in ans_arr[:ans]))


def main():
    input_text = reading()

    n = input_text[0]
    del input_text[0]

    diff = [0] * 100

    last = input_text[0]
    del input_text[0]

    for i in range(n - 1):
        a = input_text[0]
        del input_text[0]

        diff[i] = a - last
        last = a

    ans = 0
    ans_arr = [0] * 101

    if n == 1:
        ans = 1
        ans_arr[0] = 1

    for i in range(n - 1):
        d = 0
        cur_arr = [0] * 101
        cur_arr[0] = i + 1

        for j in range(i, n - 1):
            d += diff[j]

            cur_ans = 1
            cur_sum = 0

            cur_arr[cur_ans] = j + 2
            cur_ans += 1

            for k in range(j + 1, n - 1):
                cur_sum += diff[k]

                if cur_sum == d:
                    cur_arr[cur_ans] = k + 2
                    cur_ans += 1
                    cur_sum = 0

            if ans < cur_ans:
                ans = cur_ans
                ans_arr[:ans] = cur_arr[:ans]

    writing(ans, ans_arr)


if __name__ == "__main__":
    main()
