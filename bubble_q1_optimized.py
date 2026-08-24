def optimized_bubble_sort(arr):
    a = arr.copy(); passes = 0
    for i in range(len(a)-1):
        swapped = False; passes += 1
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]; swapped = True
        if not swapped: break
    if len(a) == 1: passes = 1
    return a, passes

if __name__ == "__main__":
    r,p = optimized_bubble_sort([101,102,104,103,105,107,106,108])
    assert r == sorted([101,102,104,103,105,107,106,108]) and p < 8
    assert optimized_bubble_sort([1,2,3,4,5])[1] == 1
    print("All test cases passed!")
