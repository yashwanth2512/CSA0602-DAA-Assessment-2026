"""
Experiment 12: Counting Inversions
Objective: Analyze modified merge sort.
Complexity: O(n log n)
"""

import time


def merge_and_count(arr, temp, left, mid, right):
    i, j, k = left, mid + 1, left
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for idx in range(left, right + 1):
        arr[idx] = temp[idx]

    return inv_count


def merge_sort_and_count(arr, temp, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += merge_sort_and_count(arr, temp, left, mid)
        inv_count += merge_sort_and_count(arr, temp, mid + 1, right)
        inv_count += merge_and_count(arr, temp, left, mid, right)
    return inv_count


def count_inversions(arr):
    arr = arr.copy()
    temp = [0] * len(arr)
    return merge_sort_and_count(arr, temp, 0, len(arr) - 1)


if __name__ == "__main__":
    arr = [2, 4, 1, 3, 5]

    start = time.perf_counter()
    inversions = count_inversions(arr)
    end = time.perf_counter()

    print(f"Array: {arr}")
    print(f"Number of inversions: {inversions}")
    print(f"Execution time: {end - start:.8f} seconds")

    print("\nComplexity Analysis:")
    print("Time Complexity: O(n log n) -> same divide-and-conquer structure "
          "as merge sort, with inversion counting done during the merge step")
    print("Space Complexity: O(n) -> temporary array used for merging")
    print("Explanation: Demonstrates that the merge-sort technique can be "
          "adapted to count inversions, not just sort.")
