def bubble_sort_plain(arr):
    a = arr.copy(); comparisons = 0
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            comparisons += 1
            if a[j] > a[j+1]: a[j], a[j+1] = a[j+1], a[j]
    return a, comparisons

def bubble_sort_optimized(arr):
    a = arr.copy(); comparisons = 0
    for i in range(len(a)-1):
        swapped = False
        for j in range(len(a)-1-i):
            comparisons += 1
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]; swapped = True
        if not swapped: break
    return a, comparisons

if __name__ == "__main__":
    alerts=[2,1,3,2,1,4,3,2,5,1,2,3,4,1,2]
    r1,c1=bubble_sort_plain(alerts); r2,c2=bubble_sort_optimized(alerts)
    assert r1 == r2 == sorted(alerts) and c2 <= c1
    print("Plain comparisons:",c1,"| Optimized comparisons:",c2)
    print("All test cases passed!")
