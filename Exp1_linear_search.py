"""
Experiment 1: Linear Search (Iterative)
Objective: Analyze the time complexity of linear search.
Complexity: Best (Omega) = O(1), Worst (Big-O) = O(n), Average (Theta) = Theta(n)
"""

import time


def linear_search(arr, key):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == key:
            return i, comparisons
    return -1, comparisons


if __name__ == "__main__":
    arr = [10, 25, 30, 45, 50]
    key = 30

    start = time.perf_counter()
    index, comparisons = linear_search(arr, key)
    end = time.perf_counter()

    if index != -1:
        print(f"Key found at index {index}")
    else:
        print("Key not found")

    print(f"Comparisons made: {comparisons}")
    print(f"Execution time: {end - start:.8f} seconds")

    print("\nComplexity Analysis:")
    print("Omega (best case)  : O(1)   -> key is the first element")
    print("Big-O (worst case) : O(n)   -> key is the last element or absent")
    print("Theta (average case): Theta(n) -> on average n/2 comparisons")
