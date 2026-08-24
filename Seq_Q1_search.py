"""Sequential Search - Q1: Find a given element in an array."""


def sequential_search(arr, key):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == key:
            return i, comparisons
    return -1, comparisons


if __name__ == "__main__":
    arr = [12, 25, 8, 45, 32, 19, 50]
    key = 32

    index, comparisons = sequential_search(arr, key)

    if index != -1:
        print(f"Element found at position {index + 1}")
        print(f"Number of comparisons = {comparisons}")
    else:
        print("Element not found")
        print(f"Number of comparisons = {comparisons}")
