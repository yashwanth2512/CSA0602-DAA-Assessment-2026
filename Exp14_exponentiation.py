"""
Experiment 14: Exponentiation
Objective: Compare iterative vs recursive fast power.
Complexity: Iterative O(n), Recursive fast power O(log n)
"""

import time


def power_iterative(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result


def power_fast_recursive(x, n):
    if n == 0:
        return 1
    half = power_fast_recursive(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x


if __name__ == "__main__":
    x, n = 2, 10

    start = time.perf_counter()
    iter_result = power_iterative(x, n)
    end = time.perf_counter()
    print(f"Iterative: {x}^{n} = {iter_result}")
    print(f"Iterative execution time: {end - start:.8f} seconds")

    start = time.perf_counter()
    fast_result = power_fast_recursive(x, n)
    end = time.perf_counter()
    print(f"Recursive (fast power): {x}^{n} = {fast_result}")
    print(f"Recursive execution time: {end - start:.8f} seconds")

    print("\nComplexity Analysis:")
    print("Iterative exponentiation   : O(n) -> multiplies x by itself n times")
    print("Recursive fast power       : O(log n) -> repeatedly halves the "
          "exponent using the identity x^n = (x^(n/2))^2")
    print("Explanation: The divide-and-conquer 'fast power' technique "
          "drastically reduces the number of multiplications needed.")
