"""Sequential Search - Q2: Unsuccessful search."""


def sequential_search(arr, key):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == key:
            return i, comparisons
    return -1, comparisons


if __name__ == "__main__":
    arr = [5, 10, 15, 20, 25, 30, 35]
    key = 18

    index, comparisons = sequential_search(arr, key)

    if index != -1:
        print(f"Element found at position {index + 1}")
    else:
        print("Element not found")
    print(f"Number of comparisons = {comparisons}")
