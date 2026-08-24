def insertion_sort_count_shifts(arr):
    a=arr.copy(); shifts=0
    for i in range(1,len(a)):
        key=a[i]; j=i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]; shifts+=1; j-=1
        a[j+1]=key
    return a,shifts

if __name__ == "__main__":
    import random
    log=[18.2,18.5,18.9,17.9,19.1,19.4,19.0]
    sorted_log,nearly=insertion_sort_count_shifts(log); assert sorted_log==sorted(log)
    shuffled=log.copy(); random.shuffle(shuffled)
    _,random_shifts=insertion_sort_count_shifts(shuffled)
    print("Nearly-sorted shifts:",nearly,"| Random shifts:",random_shifts)
    print("All test cases passed!")
