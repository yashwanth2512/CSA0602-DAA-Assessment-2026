"""
Experiment 5: Matrix Multiplication
Objective: Analyze nested loop complexity.
Complexity: O(n^3)
"""

import time


def matrix_multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]

    start = time.perf_counter()
    result = matrix_multiply(A, B)
    end = time.perf_counter()

    print(f"Matrix A = {A}")
    print(f"Matrix B = {B}")
    print(f"A x B = {result}")
    print(f"Execution time: {end - start:.8f} seconds")

    print("\nComplexity Analysis:")
    print("Time Complexity: O(n^3) -> three nested loops over the matrix "
          "dimensions")
    print("Space Complexity: O(n^2) -> for storing the result matrix")
    print("Explanation: Cubic growth makes naive matrix multiplication "
          "expensive for large matrices.")
