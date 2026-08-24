"""Brute Force String Matching - Q3: Comparison table for each alignment."""


def brute_force_with_table(text, pattern):
    n = len(text)
    m = len(pattern)
    positions = []

    print(f"{'Shift':<8}{'Comparisons':<14}{'Result'}")
    for i in range(n - m + 1):
        j = 0
        comparisons = 0
        while j < m:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1

        result = "Match" if j == m else "Mismatch"
        if j == m:
            positions.append(i)

        print(f"{i:<8}{comparisons:<14}{result}")

    return positions


if __name__ == "__main__":
    text = "MISSISSIPPI"
    pattern = "ISSI"

    positions = brute_force_with_table(text, pattern)

    print()
    print(f"Pattern found at position(s): {positions}")
