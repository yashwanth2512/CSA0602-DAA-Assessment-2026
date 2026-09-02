def count_inversions(arr):
    def merge(left, right):
        result = []
        i = j = 0
        inversions = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                inversions += len(left) - i
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result, inversions

    def sort(a):
        if len(a) <= 1:
            return a[:], 0

        mid = len(a) // 2
        left, x = sort(a[:mid])
        right, y = sort(a[mid:])
        merged, z = merge(left, right)

        return merged, x + y + z

    return sort(arr)


arr1 = [2, 4, 1, 3, 5]
arr2 = [4, 3, 2, 1]

for arr in [arr1, arr2]:
    sorted_arr, inversions = count_inversions(arr)
    print("Input :", arr)
    print("Sorted :", sorted_arr)
    print("Inversions :", inversions)
    print()
