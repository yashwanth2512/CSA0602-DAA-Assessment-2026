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


arr = [12, 4, 78, 23, 45, 67, 89, 1]
sorted_arr, comparisons = merge_sort(arr)
print("Sorted Array :", sorted_arr)
print("Comparisons :", comparisons)
