def count_multiplications_standard(n):
    return n ** 3


def count_multiplications_strassen(n):
    size = 1
    while size < n:
        size *= 2

    count = 1
    levels = 0
    while size > 1:
        count *= 7
        size //= 2
        levels += 1

    return count


for n in [2, 4, 8, 16, 32, 64]:
    print(
        "n =", n,
        "Standard =", count_multiplications_standard(n),
        "Strassen =", count_multiplications_strassen(n)
    )

assert count_multiplications_strassen(2) == 7
assert count_multiplications_standard(2) == 8
assert count_multiplications_strassen(4) == 49
assert count_multiplications_standard(4) == 64
assert count_multiplications_strassen(64) < count_multiplications_standard(64)

print("All test cases passed!")
