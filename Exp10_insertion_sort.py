"""
Experiment 10: Insertion Sort
Objective: Analyze iterative sorting.
Complexity: Omega = O(n), Big-O = O(n^2), Theta = Theta(n^2)
"""

import time


def insertion_sort(arr):
    arr = arr.copy()
    comparisons = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        if j >= 0:
            comparisons += 1
        arr[j + 1] = key

    return arr, comparisons


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]

    start = time.perf_counter()
    sorted_arr, comparisons = insertion_sort(arr)
    end = time.perf_counter()

    print(f"Original array: {arr}")
    print(f"Sorted array: {sorted_arr}")
    print(f"Comparisons made: {comparisons}")
    print(f"Execution time: {end - start:.8f} seconds")

    print("\nComplexity Analysis:")
    print("Omega (best case)  : O(n)   -> array is already sorted")
    print("Big-O (worst case) : O(n^2) -> array is sorted in reverse order")
    print("Theta (average case): Theta(n^2) -> roughly half the elements "
          "shift on each insertion")
    print("Explanation: Performance depends heavily on how sorted the "
          "input already is.")
