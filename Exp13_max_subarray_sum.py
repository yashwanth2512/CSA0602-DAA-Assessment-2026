"""
Experiment 13: Maximum Subarray Sum
Objective: Compare Kadane's vs divide-and-conquer.
Complexity: Kadane's O(n), Divide & Conquer O(n log n)
"""

import time


def max_subarray_kadane(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]

    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


def max_crossing_sum(arr, low, mid, high):
    left_sum = float('-inf')
    total = 0
    for i in range(mid, low - 1, -1):
        total += arr[i]
        left_sum = max(left_sum, total)

    right_sum = float('-inf')
    total = 0
    for i in range(mid + 1, high + 1):
        total += arr[i]
        right_sum = max(right_sum, total)

    return left_sum + right_sum


def max_subarray_divide_conquer(arr, low, high):
    if low == high:
        return arr[low]

    mid = (low + high) // 2

    left_max = max_subarray_divide_conquer(arr, low, mid)
    right_max = max_subarray_divide_conquer(arr, mid + 1, high)
    cross_max = max_crossing_sum(arr, low, mid, high)

    return max(left_max, right_max, cross_max)


if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]

    start = time.perf_counter()
    kadane_result = max_subarray_kadane(arr)
    end = time.perf_counter()
    print(f"Array: {arr}")
    print(f"Maximum subarray sum (Kadane's): {kadane_result}")
    print(f"Kadane's execution time: {end - start:.8f} seconds")

    start = time.perf_counter()
    dc_result = max_subarray_divide_conquer(arr, 0, len(arr) - 1)
    end = time.perf_counter()
    print(f"Maximum subarray sum (Divide & Conquer): {dc_result}")
    print(f"Divide & Conquer execution time: {end - start:.8f} seconds")

    print("\nComplexity Analysis:")
    print("Kadane's Algorithm      : O(n) time, O(1) space -> single pass "
          "tracking the best running sum")
    print("Divide & Conquer        : O(n log n) time -> array is split in "
          "half recursively, with an O(n) merge step to combine")
    print("Explanation: Kadane's is asymptotically faster, but the divide "
          "and conquer approach generalizes better to related problems.")
