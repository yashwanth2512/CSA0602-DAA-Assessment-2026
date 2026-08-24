def reorder_shelf(books):
    a = books.copy(); moves = 0
    for i in range(len(a)-1):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]: min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]; moves += 1
    return a, moves

if __name__ == "__main__":
    ordered, moves = reorder_shelf([305,102,250,118,199,400,101])
    assert ordered == sorted([305,102,250,118,199,400,101]) and moves <= len(ordered)-1
    assert reorder_shelf([100,200,300])[1] == 0
    print("All test cases passed!")
