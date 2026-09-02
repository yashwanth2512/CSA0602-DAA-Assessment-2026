"""
Experiment 3: Factorial (Iterative vs Recursive)
Objective: Compare iterative and recursive factorial computation.
Complexity: Both O(n)
"""

import time
import sys


def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    n = 5

    start = time.perf_counter()
    iter_result = factorial_iterative(n)
    end = time.perf_counter()
    print(f"Iterative factorial({n}) = {iter_result}")
    print(f"Iterative execution time: {end - start:.8f} seconds")

    start = time.perf_counter()
    rec_result = factorial_recursive(n)
    end = time.perf_counter()
    print(f"Recursive factorial({n}) = {rec_result}")
    print(f"Recursive execution time: {end - start:.8f} seconds")

    print("\nComplexity Analysis:")
    print("Iterative factorial: O(n) time, O(1) space")
    print("Recursive factorial: O(n) time, O(n) space (call stack depth = n)")
    print("Explanation: Recursion trades extra stack space for the same "
          "asymptotic time complexity as the loop-based version.")
