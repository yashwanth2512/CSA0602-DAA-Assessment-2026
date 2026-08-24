"""Sequential Search - Q4: Find all occurrences of a given element."""


def find_all_occurrences(arr, key):
    positions = []
    for i in range(len(arr)):
        if arr[i] == key:
            positions.append(i + 1)  # 1-indexed position
    return positions


if __name__ == "__main__":
    arr = [7, 12, 7, 25, 18, 7, 30, 7]
    key = 7

    positions = find_all_occurrences(arr, key)

    print("Occurrences at positions:")
    print(", ".join(str(p) for p in positions))
    print(f"Total occurrences = {len(positions)}")
