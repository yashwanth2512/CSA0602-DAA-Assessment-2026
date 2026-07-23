
n = int(input("Enter number of points: "))

points = []

print("Enter the points (x y):")

for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

comparisons = 0

print("\nConvex Hull Edges:")

for i in range(n):
    for j in range(i + 1, n):

        pos = 0
        neg = 0

        for k in range(n):

            if k == i or k == j:
                continue

            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]

            val = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

            comparisons += 1

            if val > 0:
                pos = 1
            elif val < 0:
                neg = 1

        if not (pos and neg):
            print(points[i], "->", points[j])

print("\nTotal Orientation Comparisons =", comparisons)
print("Time Complexity = O(n^3)")
