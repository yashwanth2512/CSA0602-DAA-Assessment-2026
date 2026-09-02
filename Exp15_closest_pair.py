"""
Experiment 15: Closest Pair of Points
Objective: Analyze brute force vs divide-and-conquer.
Complexity: Brute force O(n^2), Optimized (divide & conquer) O(n log n)
"""

import math
import time


def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def closest_pair_brute_force(points):
    n = len(points)
    min_dist = float('inf')
    pair = (None, None)

    for i in range(n):
        for j in range(i + 1, n):
            d = euclidean_distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])

    return pair, min_dist


def closest_pair_divide_conquer(points):
    px = sorted(points, key=lambda p: p[0])
    return _closest_pair_rec(px)


def _closest_pair_rec(px):
    n = len(px)
    if n <= 3:
        return closest_pair_brute_force(px)

    mid = n // 2
    mid_point = px[mid]

    left_pair, left_dist = _closest_pair_rec(px[:mid])
    right_pair, right_dist = _closest_pair_rec(px[mid:])

    if left_dist <= right_dist:
        best_pair, best_dist = left_pair, left_dist
    else:
        best_pair, best_dist = right_pair, right_dist

    strip = [p for p in px if abs(p[0] - mid_point[0]) < best_dist]
    strip.sort(key=lambda p: p[1])

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) >= best_dist:
                break
            d = euclidean_distance(strip[i], strip[j])
            if d < best_dist:
                best_dist = d
                best_pair = (strip[i], strip[j])

    return best_pair, best_dist


if __name__ == "__main__":
    points = [(1, 2), (4, 5), (7, 8), (3, 1)]

    start = time.perf_counter()
    bf_pair, bf_dist = closest_pair_brute_force(points)
    end = time.perf_counter()
    print(f"Points: {points}")
    print(f"Brute Force -> Closest pair: {bf_pair[0]} - {bf_pair[1]}, "
          f"Distance = {bf_dist}")
    print(f"Brute Force execution time: {end - start:.8f} seconds")

    start = time.perf_counter()
    dc_pair, dc_dist = closest_pair_divide_conquer(points)
    end = time.perf_counter()
    print(f"Divide & Conquer -> Closest pair: {dc_pair[0]} - {dc_pair[1]}, "
          f"Distance = {dc_dist}")
    print(f"Divide & Conquer execution time: {end - start:.8f} seconds")

    print("\nComplexity Analysis:")
    print("Brute Force        : O(n^2) -> compares every pair of points")
    print("Divide & Conquer   : O(n log n) -> recursively splits points and "
          "merges results using a bounded 'strip' check")
    print("Explanation: Brute force is quadratic, motivating the more "
          "scalable divide-and-conquer approach for large point sets.")
