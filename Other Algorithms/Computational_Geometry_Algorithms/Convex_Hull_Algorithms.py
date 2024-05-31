def graham_scan(points):
    points = sorted(points)
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

if __name__ == "__main__":
    points = [(0, 3), (1, 1), (2, 2), (4, 4),
              (0, 0), (1, 2), (3, 1), (3, 3)]
    hull = graham_scan(points)
    print(f"Convex Hull: {hull}")
