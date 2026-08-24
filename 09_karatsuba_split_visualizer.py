def karatsuba_traced(x, y):
    trace = []

    def solve(a, b, depth):
        if a < 10 or b < 10:
            trace.append((depth, a, b, None, None, None, None))
            return a * b

        n = max(len(str(a)), len(str(b)))
        half = n // 2
        p = 10 ** half

        high1, low1 = divmod(a, p)
        high2, low2 = divmod(b, p)

        trace.append((depth, a, b, high1, low1, high2, low2))

        z2 = solve(high1, high2, depth + 1)
        z0 = solve(low1, low2, depth + 1)
        z1 = solve(high1 + low1, high2 + low2, depth + 1) - z2 - z0

        return z2*p*p + z1*p + z0

    result = solve(x, y, 0)
    return result, trace


result, trace = karatsuba_traced(1234, 56)

assert result == 1234 * 56
assert len(trace) > 0
assert trace[0][0] == 0

for item in trace:
    print(item)

print("All test cases passed!")
