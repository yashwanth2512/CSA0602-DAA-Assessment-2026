def quick_sort(arr):
    a = arr[:]
    comparisons = [0]

    def partition(low, high):
        pivot = a[high]
        i = low - 1

        for j in range(low, high):
            comparisons[0] += 1
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]

        a[i + 1], a[high] = a[high], a[i + 1]
        return i + 1

    def sort(low, high):
        if low < high:
            p = partition(low, high)
            sort(low, p - 1)
            sort(p + 1, high)

    sort(0, len(a) - 1)
    return a, comparisons[0]


arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr, comparisons = quick_sort(arr)
print("Sorted Array :", sorted_arr)
print("Comparisons :", comparisons)
