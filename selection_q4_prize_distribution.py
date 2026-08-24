def distribute_prizes(participants):
    a = participants.copy()
    for i in range(len(a)-1):
        max_idx = i
        for j in range(i+1, len(a)):
            if a[j][1] > a[max_idx][1]: max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]
    return a

if __name__ == "__main__":
    ranking = distribute_prizes([("Asha",88),("Ravi",95),("Meera",79),("Dev",95)])
    scores = [p[1] for p in ranking]
    assert scores == sorted(scores, reverse=True) and ranking[0][1] == 95
    print("All test cases passed!")
