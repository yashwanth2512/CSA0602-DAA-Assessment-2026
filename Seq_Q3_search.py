"""Sequential Search - Q3: First occurrence of an element."""


def find_first_occurrence(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


if __name__ == "__main__":
    arr = [10, 25, 15, 25, 30, 25, 40]
    key = 25

    index = find_first_occurrence(arr, key)

    if index != -1:
        print(f"First occurrence at position {index + 1}")
    else:
        print("Element not found")
