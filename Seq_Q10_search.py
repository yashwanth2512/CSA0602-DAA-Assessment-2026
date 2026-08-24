"""Sequential Search - Q10: Implement and analyze performance."""


def sequential_search_verbose(arr, key):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        print(f"Comparing arr[{i}] = {arr[i]} with key = {key}")
        if arr[i] == key:
            return i, comparisons
    return -1, comparisons


if __name__ == "__main__":
    arr = [45, 23, 67, 12, 89, 34, 56, 78, 90, 11, 29, 73, 18, 64, 37]
    search_keys = [73, 18, 100]

    for key in search_keys:
        print(f"--- Searching for key = {key} ---")
        index, comparisons = sequential_search_verbose(arr, key)
        if index != -1:
            print(f"Found at position {index + 1}")
        else:
            print("Not found")
        print(f"Number of comparisons = {comparisons}")
        print()

    n = len(arr)
    print("Performance Analysis:")
    print(f"Best-case complexity   : O(1)   -> element found at the first position "
          f"(e.g. key = {arr[0]})")
    print(f"Average-case complexity: O(n)   -> on average about n/2 = {n // 2} "
          f"comparisons for a successful search")
    print(f"Worst-case complexity  : O(n)   -> element at the last position or "
          f"absent (e.g. key = 100, {n} comparisons)")
    print("Space complexity       : O(1)   -> no extra space is used besides "
          "the input array")
