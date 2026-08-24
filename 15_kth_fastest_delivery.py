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


def kth_smallest_delivery_time(delivery_times, k):
    return median_of_medians_select(delivery_times, k)


already_sorted = list(range(1, 501))

assert kth_smallest_delivery_time(already_sorted, 0) == 1
assert kth_smallest_delivery_time(already_sorted, 499) == 500
assert kth_smallest_delivery_time(already_sorted, 250) == 251

delivery_times = [45,30,60,25,50,40,35,55,20,65]

assert kth_smallest_delivery_time(
    delivery_times, 0
) == min(delivery_times)

print("1st Fastest:", kth_smallest_delivery_time(delivery_times, 0))
print("All test cases passed!")
