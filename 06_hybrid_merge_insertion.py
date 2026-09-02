def insertion_sort(arr):
    a = arr[:]

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a


def hybrid_merge_sort(arr, threshold=4):
    def merge(left, right):
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

    def sort(a):
        if len(a) <= threshold:
            return insertion_sort(a)

        mid = len(a) // 2
        left = sort(a[:mid])
        right = sort(a[mid:])
        return merge(left, right)

    return sort(arr)


arr1 = [12, 11, 13, 5, 6, 7, 3, 2]
arr2 = [9, 4, 6, 2, 8, 1]

print("Input :", arr1)
print("Sorted :", hybrid_merge_sort(arr1))

print("\nInput :", arr2)
print("Sorted :", hybrid_merge_sort(arr2))
