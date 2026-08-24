import math


def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


def brute_force_closest(points):
    best_pair = None
    best_distance = float("inf")

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i], points[j])
            if d < best_distance:
                best_distance = d
                best_pair = (points[i], points[j])

    return best_pair, best_distance


def closest_pair_of_points(points):
    points = sorted(points, key=lambda p: (p[0], p[1]))

    def solve(px):
        if len(px) <= 3:
            return brute_force_closest(px)

        mid = len(px) // 2
        left = px[:mid]
        right = px[mid:]
        mid_x = px[mid][0]

        pair1, d1 = solve(left)
        pair2, d2 = solve(right)

        if d1 <= d2:
            best_pair, d = pair1, d1
        else:
            best_pair, d = pair2, d2

        strip = [p for p in px if abs(p[0] - mid_x) < d]
        strip.sort(key=lambda p: p[1])

        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and strip[j][1] - strip[i][1] < d:
                current = distance(strip[i], strip[j])
                if current < d:
                    d = current
                    best_pair = (strip[i], strip[j])
                j += 1

        return best_pair, d

    return solve(points)


pts = [(2,3),(12,30),(40,50),(5,1),(12,10),(3,4)]
pair, d = closest_pair_of_points(pts)
brute_pair, brute_d = brute_force_closest(pts)

assert abs(d - brute_d) < 1e-9

print("Closest Pair :", pair)
print("Distance :", d)
print("All test cases passed!")
