"""Brute Force String Matching - Q2: Find all occurrences of a pattern."""


def brute_force_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    positions = []

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            positions.append(i)

    return positions


if __name__ == "__main__":
    text = "BANANABANANA"
    pattern = "ANA"

    positions = brute_force_string_match(text, pattern)

    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    print(f"Occurrences at positions {', '.join(str(p) for p in positions)}.")
