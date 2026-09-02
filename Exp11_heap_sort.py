"""
Experiment 11: Heap Sort
Objective: Analyze heap-based sorting.
Complexity: Always O(n log n)
"""

import time


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


if __name__ == "__main__":
    arr = [4, 10, 3, 5, 1]

    start = time.perf_counter()
    sorted_arr = heap_sort(arr)
    end = time.perf_counter()

    print(f"Original array: {arr}")
    print(f"Sorted array: {sorted_arr}")
    print(f"Execution time: {end - start:.8f} seconds")

    print("\nComplexity Analysis:")
    print("Time Complexity: O(n log n) in the best, average, and worst cases")
    print("Space Complexity: O(1) -> sorts in place using the heap structure")
    print("Explanation: Building the heap takes O(n), and each of the n "
          "extractions takes O(log n), giving O(n log n) overall.")
