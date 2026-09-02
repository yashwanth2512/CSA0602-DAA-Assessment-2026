import time


def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def measure(arr):
    start = time.perf_counter()
    result = merge_sort(arr)
    end = time.perf_counter()
    return result, end - start


arr1 = [9, 8, 7, 6, 5, 4, 3]
arr2 = [1, 2, 3, 4, 5, 6]

result, elapsed = measure(arr1)
print("Reverse Sorted Input :", arr1)
print("Sorted Output :", result)
print("Time Taken : %.10f sec" % elapsed)

result, elapsed = measure(arr2)
print("\nSorted Input :", arr2)
print("Sorted Output :", result)
print("Time Taken : %.10f sec" % elapsed)
