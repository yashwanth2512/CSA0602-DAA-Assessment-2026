def top_k_scores(scores, k):
    a = scores.copy()
    result = []
    k = min(k, len(a))
    for i in range(k):
        max_idx = i
        for j in range(i + 1, len(a)):
            if a[j] > a[max_idx]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]
        result.append(a[i])
    return result

if __name__ == "__main__":
    assert top_k_scores([72,88,65,90,77,95,60,83,91,68], 5) == [95,91,90,88,83]
    assert top_k_scores([5,3,1], 5) == [5,3,1]
    assert top_k_scores([], 3) == []
    print("All test cases passed!")
