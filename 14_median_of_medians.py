def median_of_medians_select(data, k):
    if not 0 <= k < len(data):
        raise ValueError("k must be a valid zero-based index")

    if len(data) <= 5:
        return sorted(data)[k]

    groups = [data[i:i+5] for i in range(0, len(data), 5)]
    medians = [sorted(group)[len(group)//2] for group in groups]

    pivot = median_of_medians_select(medians, len(medians)//2)

    low = [x for x in data if x < pivot]
    equal = [x for x in data if x == pivot]
    high = [x for x in data if x > pivot]

    if k < len(low):
        return median_of_medians_select(low, k)

    if k < len(low) + len(equal):
        return pivot

    return median_of_medians_select(
        high, k - len(low) - len(equal)
    )


data = [12, 3, 5, 7, 4, 19, 26]

for k in range(len(data)):
    assert median_of_medians_select(data, k) == sorted(data)[k]

print("Data:", data)
print("Median:", median_of_medians_select(data, len(data)//2))

print("All test cases passed!")
