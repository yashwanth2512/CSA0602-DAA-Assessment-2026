def selection_sort_min_writes(arr):
    a = arr.copy(); swaps = 0
    for i in range(len(a)-1):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1
    return a, swaps

if __name__ == "__main__":
    res, sw = selection_sort_min_writes([23.5,19.2,25.1,18.8,21.4])
    assert res == sorted([23.5,19.2,25.1,18.8,21.4]) and sw <= len(res)-1
    res2, sw2 = selection_sort_min_writes([1,2,3,4,5])
    assert sw2 == 0
    print("All test cases passed!")
