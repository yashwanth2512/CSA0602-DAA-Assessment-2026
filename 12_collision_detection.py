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


def detect_potential_collision(sprites, threshold):
    pair, min_dist = closest_pair(sprites)

    if min_dist <= threshold:
        return pair, min_dist

    return None, min_dist


sprites = [(0,0), (1,1), (50,50), (100,100), (1.2,0.9)]
pair, min_dist = detect_potential_collision(sprites, threshold=2.0)

assert pair is not None and min_dist <= 2.0

far_sprites = [(0,0), (100,100), (200,200)]
pair2, min_dist2 = detect_potential_collision(far_sprites, threshold=1.0)

assert pair2 is None

print("Collision Pair :", pair)
print("Minimum Distance :", min_dist)
print("All test cases passed!")
