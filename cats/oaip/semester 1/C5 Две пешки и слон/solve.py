def check():
    if (abs(x1 - x2) == abs(y1 - y2)) or (x1 + y1 == x2+y2):
        for x in range(min(x1, x2), max(x1, x2) - 1):
            for y in range(min(y1, y2), max(y1, y2) - 1):
                if desk[x][y] == 2 and (y != y1 or y != y2) and (x != x1 or x != x2):
                    return y + 1, x + 1
    else:
        for i in range(8):
            for j in range(8):
                if desk[i][j] == 2:
                    return j + 1, i + 1


def good_move(x, y):
    return 0 <= x < 8 and 0 <= y < 8


def fill(x, y):
    for i in range(9):
        new_x = x + i - 1
        new_y = y + i - 1
        new_x_back = x - i - 2
        new_y_back = y - i - 2

        if good_move(new_x, new_y):
            desk[new_x][new_y] += 1
        if good_move(new_x_back, new_y_back):
            desk[new_x_back][new_y_back] += 1

    for i in range(1, 9):
        new_x = x - i - 1
        new_y = y + i - 1
        new_x_back = x + i - 1
        new_y_back = y - i - 1

        if good_move(new_x, new_y):
            desk[new_x][new_y] += 1
        if good_move(new_x_back, new_y_back):
            desk[new_x_back][new_y_back] += 1


with open("input.txt", "r", encoding="utf-8") as f, open("output.txt", "w", encoding="utf-8") as q:
    desk = [[0] * 8 for i in range(8)]
    y1, x1, y2, x2 = map(int, f.readline().split())
    fill(x1, y1)
    fill(x2, y2)
    res = check() if check() else "0"
    print(*res)
    q.write(" ".join(list(map(str, res))))
    # for i in desk:
    #     for j in i:
    #         print(str(j).ljust(3), end="")
    #     print()
