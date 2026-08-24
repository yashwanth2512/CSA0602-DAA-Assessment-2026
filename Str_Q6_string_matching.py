"""Brute Force String Matching - Q6: Report first occurrence only."""


def brute_force_first_occurrence(text, pattern):
    n = len(text)
    m = len(pattern)
    total_comparisons = 0

    for i in range(n - m + 1):
        j = 0
        while j < m:
            total_comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == m:
            return i, total_comparisons

    return -1, total_comparisons


if __name__ == "__main__":
    text = "COMPUTERSCIENCE"
    pattern = "SCI"

    position, comparisons = brute_force_first_occurrence(text, pattern)

    if position != -1:
        print(f"First occurrence position: {position}")
    else:
        print("Pattern not found")
    print(f"Number of comparisons: {comparisons}")
