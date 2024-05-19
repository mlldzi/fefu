def longest_capture(board):
    N = len(board)
    longest_path = []

    def explore_captures(row, col, path):
        nonlocal longest_path

        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            r, c = row + dr, col + dc
            if 0 <= r < N and 0 <= c < N and board[r][c] == 'O':
                r2, c2 = r + dr, c + dc
                if 0 <= r2 < N and 0 <= c2 < N and board[r2][c2] == '.':
                    board[row][col] = '.'
                    board[r][c] = '.'

                    move = f"{chr(97 + col)}{N - row}-{chr(97 + c2)}{N - r2}"
                    path.append(move)
                    explore_captures(r2, c2, path)

                    board[row][col] = 'X'
                    board[r][c] = 'O'
                    path.pop()

        if len(path) > len(longest_path):
            longest_path = path[:]

    for row in range(N):
        for col in range(N):
            if board[row][col] == 'X':
                explore_captures(row, col, [])

    return "-".join(longest_path) if longest_path else "Impossible"


def reading():
    with open("input.txt") as f:
        N = int(f.readline())
        board = [list(f.readline().strip()) for _ in range(N)]
    return board


def writing(res):
    with open("output.txt", "w") as f:
        f.write(res)


def main():
    board = reading()
    res = longest_capture(board).split("-")
    result = []
    for i in range(len(res)):
        if i == 0:
            continue
            
        prev = res[i - 1]
        curr = res[i]
        if prev != curr:
            result.append(res[i - 1])
    result.append(res[-1])
    result = "-".join(result)
    writing(result)


if __name__ == "__main__":
    main()
