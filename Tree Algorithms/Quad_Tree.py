class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def contains(self, point):
        return (self.x - self.w <= point.x < self.x + self.w and
                self.y - self.h <= point.y < self.y + self.h)

    def intersects(self, range):
        return not (range.x - range.w > self.x + self.w or
                    range.x + range.w < self.x - self.w or
                    range.y - range.h > self.y + self.h or
                    range.y + range.h < self.y - self.h)

class QuadTree:
    def __init__(self, boundary, capacity):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False

    def subdivide(self):
        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.w / 2
        h = self.boundary.h / 2

        ne = Rectangle(x + w, y - h, w, h)
        self.northeast = QuadTree(ne, self.capacity)
        nw = Rectangle(x - w, y - h, w, h)
        self.northwest = QuadTree(nw, self.capacity)
        se = Rectangle(x + w, y + h, w, h)
        self.southeast = QuadTree(se, self.capacity)
        sw = Rectangle(x - w, y + h, w, h)
        self.southwest = QuadTree(sw, self.capacity)

        self.divided = True

    def insert(self, point):
        if not self.boundary.contains(point):
            return False

        if len(self.points) < self.capacity:
            self.points.append(point)
            return True
        else:
            if not self.divided:
                self.subdivide()

            if self.northeast.insert(point):
                return True
            elif self.northwest.insert(point):
                return True
            elif self.southeast.insert(point):
                return True
            elif self.southwest.insert(point):
                return True

    def query(self, range, found):
        if not self.boundary.intersects(range):
            return
        else:
            for p in self.points:
                if range.contains(p):
                    found.append(p)
            if self.divided:
                self.northwest.query(range, found)
                self.northeast.query(range, found)
                self.southwest.query(range, found)
                self.southeast.query(range, found)

if __name__ == "__main__":
    boundary = Rectangle(200, 200, 200, 200)
    qt = QuadTree(boundary, 4)
    points = [Point(100, 100), Point(150, 150), Point(250, 250), Point(300, 300)]
    for p in points:
        qt.insert(p)

    range = Rectangle(200, 200, 50, 50)
    found_points = []
    qt.query(range, found_points)
    print("Found points:")
    for p in found_points:
        print(f"({p.x}, {p.y})")
