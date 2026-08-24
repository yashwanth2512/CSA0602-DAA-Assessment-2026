import math


def closest_pair(points):
    best_pair = None
    best_distance = float("inf")

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = math.hypot(
                points[i][0] - points[j][0],
                points[i][1] - points[j][1]
            )
            if d < best_distance:
                best_distance = d
                best_pair = (points[i], points[j])

    return best_pair, best_distance


def check_minimum_spacing(nodes, min_safe_distance):
    pair, min_dist = closest_pair(nodes)
    ok = min_dist >= min_safe_distance
    return ok, pair, min_dist


nodes = [(0,0), (10,10), (10.5,10.2), (30,40), (31,41)]
ok, pair, min_dist = check_minimum_spacing(nodes, min_safe_distance=1.0)

assert ok is False

spaced_nodes = [(0,0), (10,10), (20,20), (30,30)]
ok2, _, _ = check_minimum_spacing(spaced_nodes, min_safe_distance=1.0)

assert ok2 is True

print("Safe Spacing:", ok)
print("Closest Pair:", pair)
print("Minimum Distance:", min_dist)
print("All test cases passed!")
