def bubble_sort_hand(hand):
    a = hand.copy(); passes = 0
    for i in range(len(a)-1):
        swapped=False; passes += 1
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]; swapped=True
        if not swapped: break
    return a, passes

if __name__ == "__main__":
    import random
    hand=[2,4,6,8,9,11,13]; hand.append(7)
    final,p_inc=bubble_sort_hand(hand); assert final==sorted(hand)
    shuffled=hand.copy(); random.shuffle(shuffled)
    _,p_full=bubble_sort_hand(shuffled); assert p_inc<=p_full
    print("All test cases passed!")
