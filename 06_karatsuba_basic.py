def karatsuba(x, y):
    sign = -1 if (x < 0) != (y < 0) else 1
    x, y = abs(x), abs(y)

    if x < 10 or y < 10:
        return sign * x * y

    n = max(len(str(x)), len(str(y)))
    half = n // 2
    power = 10 ** half

    high1, low1 = divmod(x, power)
    high2, low2 = divmod(y, power)

    z2 = karatsuba(high1, high2)
    z0 = karatsuba(low1, low2)
    z1 = karatsuba(high1 + low1, high2 + low2) - z2 - z0

    return sign * (z2 * power * power + z1 * power + z0)


assert karatsuba(1234, 5678) == 1234 * 5678
assert karatsuba(123456789, 987654321) == 123456789 * 987654321
assert karatsuba(9, 9) == 81
assert karatsuba(0, 12345) == 0

big1, big2 = int("9"*50), int("8"*50)
assert karatsuba(big1, big2) == big1 * big2

print("All test cases passed!")
