"""Brute Force String Matching - Q1: Find pattern occurrences and total comparisons."""


def brute_force_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    positions = []
    total_comparisons = 0

    for i in range(n - m + 1):
        j = 0
        while j < m:
            total_comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == m:
            positions.append(i)

    return positions, total_comparisons


if __name__ == "__main__":
    text = "AABAACAADAABAABA"
    pattern = "AABA"

    positions, comparisons = brute_force_string_match(text, pattern)

    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    print(f"Position(s) where the pattern occurs: {positions}")
    print(f"Total number of comparisons: {comparisons}")
