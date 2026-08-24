def multiply_polynomials_naive(p1, p2):
    result = [0] * (len(p1) + len(p2) - 1)

    for i in range(len(p1)):
        for j in range(len(p2)):
            result[i + j] += p1[i] * p2[j]

    return result


def add_poly(a, b):
    n = max(len(a), len(b))
    result = [0] * n

    for i in range(n):
        if i < len(a):
            result[i] += a[i]
        if i < len(b):
            result[i] += b[i]

    return result


def subtract_poly(a, b):
    n = max(len(a), len(b))
    result = [0] * n

    for i in range(n):
        if i < len(a):
            result[i] += a[i]
        if i < len(b):
            result[i] -= b[i]

    return result


def add_shifted(result, value, shift):
    if len(result) < len(value) + shift:
        result.extend([0] * (len(value) + shift - len(result)))

    for i in range(len(value)):
        result[i + shift] += value[i]


def karatsuba_poly(p1, p2):
    if not p1 or not p2:
        return [0]

    if len(p1) == 1 or len(p2) == 1:
        return multiply_polynomials_naive(p1, p2)

    n = max(len(p1), len(p2))
    if n <= 2:
        return multiply_polynomials_naive(p1, p2)

    m = n // 2

    low1, high1 = p1[:m], p1[m:]
    low2, high2 = p2[:m], p2[m:]

    z0 = karatsuba_poly(low1, low2)
    z2 = karatsuba_poly(high1, high2)

    s1 = add_poly(low1, high1)
    s2 = add_poly(low2, high2)

    z1 = karatsuba_poly(s1, s2)
    z1 = subtract_poly(subtract_poly(z1, z2), z0)

    result = [0] * (len(p1) + len(p2) - 1)
    add_shifted(result, z0, 0)
    add_shifted(result, z1, m)
    add_shifted(result, z2, 2*m)

    return result


assert multiply_polynomials_naive([1, 2], [3, 4]) == [3, 10, 8]

p1, p2 = [1, 2, 3, 4], [5, 6, 7, 8]
naive_result = multiply_polynomials_naive(p1, p2)
karatsuba_result = karatsuba_poly(p1, p2)

assert karatsuba_result == naive_result

print("Naive:", naive_result)
print("Karatsuba:", karatsuba_result)
print("All test cases passed!")
