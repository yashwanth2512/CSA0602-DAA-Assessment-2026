import time

def selection_sort(arr):
    a = arr.copy()
    for i in range(len(a)-1):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]: min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

if __name__ == "__main__":
    data = [499,129,899,45,275,60,310,150]
    start = time.perf_counter()
    result = selection_sort(data)
    elapsed = time.perf_counter() - start
    assert result == sorted(data)
    assert selection_sort([]) == [] and selection_sort([7]) == [7]
    print("Sorted:", result)
    print("Time:", elapsed)
    print("All test cases passed!")
