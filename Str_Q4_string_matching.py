"""Brute Force String Matching - Q4: Count comparisons, matches, mismatches."""


def brute_force_stats(text, pattern):
    n = len(text)
    m = len(pattern)
    total_comparisons = 0
    total_matches = 0
    total_mismatches = 0
    positions = []

    for i in range(n - m + 1):
        j = 0
        while j < m:
            total_comparisons += 1
            if text[i + j] == pattern[j]:
                total_matches += 1
            else:
                total_mismatches += 1
                break
            j += 1
        if j == m:
            positions.append(i)

    return positions, total_comparisons, total_matches, total_mismatches


if __name__ == "__main__":
    text = "ABABABABAB"
    pattern = "ABAB"

    positions, comparisons, matches, mismatches = brute_force_stats(text, pattern)

    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    print(f"Pattern found at positions: {positions}")
    print(f"Total character comparisons = {comparisons}")
    print(f"Total matches = {matches}")
    print(f"Total mismatches = {mismatches}")
