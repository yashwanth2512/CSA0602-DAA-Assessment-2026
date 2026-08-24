"""Sequential Search - Q5: Count comparisons, matches, mismatches."""


def sequential_search_stats(arr, key):
    comparisons = 0
    matches = 0
    mismatches = 0
    found_at = -1

    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == key:
            matches += 1
            found_at = i
            break
        else:
            mismatches += 1

    return found_at, comparisons, matches, mismatches


if __name__ == "__main__":
    arr = [3, 6, 9, 12, 15, 18, 21]
    key = 15

    index, comparisons, matches, mismatches = sequential_search_stats(arr, key)

    if index != -1:
        print(f"Element found at position {index + 1}")
    else:
        print("Element not found")

    print(f"Total comparisons = {comparisons}")
    print(f"Total matches = {matches}")
    print(f"Total mismatches = {mismatches}")
