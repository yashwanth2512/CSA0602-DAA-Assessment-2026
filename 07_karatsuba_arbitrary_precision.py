def schoolbook_multiply(x, y):
    return x * y


def karatsuba(x, y):
    sign = -1 if (x < 0) != (y < 0) else 1
    x, y = abs(x), abs(y)

    if x < 10 or y < 10:
        return sign * x * y

    n = max(len(str(x)), len(str(y)))
    half = n // 2
    p = 10 ** half

    a, b = divmod(x, p)
    c, d = divmod(y, p)

    z2 = karatsuba(a, c)
    z0 = karatsuba(b, d)
    z1 = karatsuba(a + b, c + d) - z2 - z0

    return sign * (z2 * p * p + z1 * p + z0)


for digits in [2, 4, 8, 16, 32]:
    x = int("7" * digits)
    y = int("3" * digits)

    assert karatsuba(x, y) == schoolbook_multiply(x, y)
    print("Digits:", digits, "Result verified")

print("All test cases passed!")
