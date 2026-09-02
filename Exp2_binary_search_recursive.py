"""
Experiment 2: Binary Search (Recursive)
Objective: Compare recursive binary search complexity.
Complexity: Best (Omega) = O(1), Worst (Big-O) = O(log n), Average (Theta) = Theta(log n)
"""

import time


def binary_search_recursive(arr, key, low, high, depth=0):
    if low > high:
        return -1, depth

    mid = (low + high) // 2
    depth += 1

    if arr[mid] == key:
        return mid, depth
    elif arr[mid] < key:
        return binary_search_recursive(arr, key, mid + 1, high, depth)
    else:
        return binary_search_recursive(arr, key, low, mid - 1, depth)


if __name__ == "__main__":
    arr = [5, 10, 15, 20, 25]
    key = 20

    start = time.perf_counter()
    index, comparisons = binary_search_recursive(arr, key, 0, len(arr) - 1)
    end = time.perf_counter()

    if index != -1:
        print(f"Key found at index {index}")
    else:
        print("Key not found")

    print(f"Recursive calls (comparisons): {comparisons}")
    print(f"Execution time: {end - start:.8f} seconds")

    print("\nComplexity Analysis:")
    print("Omega (best case)  : O(1)      -> key found at the middle on first call")
    print("Big-O (worst case) : O(log n)  -> key found near the end of recursion or absent")
    print("Theta (average case): Theta(log n) -> search space halves each call")
