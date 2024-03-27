def calculate_minimum_board_size(W, H, N):
    left = 1
    right = max(W, H) * N

    while left < right:
        mid = (left + right) // 2
        rows = mid // W
        cols = mid // H
        total_diplomas = rows * cols

        if total_diplomas >= N:
            right = mid
        else:
            left = mid + 1

    return left

with open("diploma.in", "r") as file:
    W, H, N = map(int, file.readline().split())

minimum_size = calculate_minimum_board_size(W, H, N)

with open("diploma.out", "w") as file:
    file.write(str(minimum_size))