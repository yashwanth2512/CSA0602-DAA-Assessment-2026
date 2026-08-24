def bubble_sort_with_frames(arr):
    a = arr.copy(); frames = [a.copy()]
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]: a[j], a[j+1] = a[j+1], a[j]
        frames.append(a.copy())
    return frames

if __name__ == "__main__":
    frames = bubble_sort_with_frames([5,1,4,2,8])
    assert frames[-1] == sorted([5,1,4,2,8])
    assert frames[0] == [5,1,4,2,8] and len(frames) >= 2
    print("Frames:", frames)
    print("All test cases passed!")
