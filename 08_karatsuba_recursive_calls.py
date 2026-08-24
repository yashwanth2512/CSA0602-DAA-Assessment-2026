def karatsuba_with_count(x, y, counter):
    counter[0] += 1

    if x < 0 or y < 0:
        return (-1 if (x < 0) != (y < 0) else 1) * \
               karatsuba_with_count(abs(x), abs(y), counter)

    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    half = n // 2
    p = 10 ** half

    a, b = divmod(x, p)
    c, d = divmod(y, p)

    z2 = karatsuba_with_count(a, c, counter)
    z0 = karatsuba_with_count(b, d, counter)
    z1 = karatsuba_with_count(a+b, c+d, counter) - z2 - z0

    return z2*p*p + z1*p + z0


for digits in [2, 4, 8, 16]:
    x = int("7" * digits)
    y = int("3" * digits)
    counter = [0]

    result = karatsuba_with_count(x, y, counter)

    print("Digits:", digits)
    print("Recursive Calls:", counter[0])
    assert result == x * y

counter2 = [0]
assert karatsuba_with_count(9, 9, counter2) == 81
assert counter2[0] == 1

print("All test cases passed!")
