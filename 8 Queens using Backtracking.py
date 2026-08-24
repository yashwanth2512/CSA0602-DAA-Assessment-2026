
N = 8

board = [[0] * N for _ in range(N)]


def is_safe(row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i = row - 1
    j = col + 1

    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(row):

    if row == N:
        return True

    for col in range(N):

        if is_safe(row, col):
            board[row][col] = 1

            if solve(row + 1):
                return True

            board[row][col] = 0

    return False


if solve(0):

    print("8-Queens Solution:\n")

    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))

else:
    print("No solution")
