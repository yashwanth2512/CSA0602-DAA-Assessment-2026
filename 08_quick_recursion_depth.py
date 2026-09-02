def quick_sort_depth(arr):
    a = arr[:]
    max_depth = [0]

    def partition(low, high):
        pivot = a[high]
        i = low - 1

        for j in range(low, high):
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]

        a[i + 1], a[high] = a[high], a[i + 1]
        return i + 1

    def sort(low, high, depth):
        if low < high:
            max_depth[0] = max(max_depth[0], depth)
            p = partition(low, high)
            sort(low, p - 1, depth + 1)
            sort(p + 1, high, depth + 1)

    if a:
        sort(0, len(a) - 1, 1)

    return a, max_depth[0]


arr1 = [10, 7, 8, 9, 1, 5]
arr2 = [1, 2, 3, 4, 5]

for arr in [arr1, arr2]:
    result, depth = quick_sort_depth(arr)
    print("Input :", arr)
    print("Sorted :", result)
    print("Max Depth :", depth)
    print()
