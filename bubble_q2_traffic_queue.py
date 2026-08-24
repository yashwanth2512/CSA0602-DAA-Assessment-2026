def bubble_sort_queue(queue):
    priority = {"ambulance": 3, "bus": 2, "car": 1}
    a = queue.copy()
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if priority[a[j]] < priority[a[j+1]]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

if __name__ == "__main__":
    q = ["car","car","bus"]; q.append("ambulance")
    assert bubble_sort_queue(q) == ["ambulance","bus","car","car"]
    assert bubble_sort_queue(["ambulance"]) == ["ambulance"]
    print("All test cases passed!")
