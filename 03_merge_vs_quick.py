def merge_sort(arr):
    comparisons = [0]

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparisons[0] += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def divide(a):
        if len(a) <= 1:
            return a[:]
        mid = len(a) // 2
        return merge(divide(a[:mid]), divide(a[mid:]))

    return divide(arr), comparisons[0]


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


arr = [12, 11, 13, 5, 6, 7]

m_sorted, m_count = merge_sort(arr)
q_sorted, q_count = quick_sort(arr)

print("Sorted Array :", m_sorted)
print("Merge Comparisons :", m_count)
print("Quick Comparisons :", q_count)

if m_count < q_count:
    print("Better Algorithm : Merge Sort")
elif q_count < m_count:
    print("Better Algorithm : Quick Sort")
else:
    print("Both are equal for this input")
