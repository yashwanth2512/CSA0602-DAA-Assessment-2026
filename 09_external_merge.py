def external_merge(a, b):
    result = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])
    return result


a1 = [1, 3, 5]
b1 = [2, 4, 6]

a2 = [10, 20]
b2 = [5, 15, 25]

print("Merged 1 :", external_merge(a1, b1))
print("Merged 2 :", external_merge(a2, b2))
