def kth_smallest(arr, k):
    if k < 1 or k > len(arr):
        raise ValueError("k must be between 1 and N")

    a = arr[:]
    target = k - 1
    low = 0
    high = len(a) - 1

    def partition(low, high):
        pivot = a[high]
        i = low - 1

        for j in range(low, high):
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]

        a[i + 1], a[high] = a[high], a[i + 1]
        return i + 1

    while low <= high:
        p = partition(low, high)

        if p == target:
            return a[p]
        elif target < p:
            high = p - 1
        else:
            low = p + 1


arr1 = [7, 10, 4, 3, 20, 15]
arr2 = [12, 3, 5, 7, 19]

print("Array 1 :", arr1)
print("3rd Smallest :", kth_smallest(arr1, 3))

print("\nArray 2 :", arr2)
print("2nd Smallest :", kth_smallest(arr2, 2))
