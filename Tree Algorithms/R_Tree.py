class Rectangle:
    def __init__(self, x_min, x_max, y_min, y_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def intersects(self, other):
        return not (self.x_min > other.x_max or self.x_max < other.x_min or
                    self.y_min > other.y_max or self.y_max < other.y_min)

class RTreeNode:
    def __init__(self, mbr, is_leaf=False):
        self.mbr = mbr
        self.is_leaf = is_leaf
        self.children = []

class RTree:
    def __init__(self):
        self.root = RTreeNode(Rectangle(float('-inf'), float('inf'), float('-inf'), float('inf')))

    def insert(self, rect):
        leaf = self.choose_leaf(self.root, rect)
        leaf.children.append(RTreeNode(rect, True))
        self.adjust_tree(leaf)

    def choose_leaf(self, node, rect):
        if node.is_leaf:
            return node
        best_child = node.children[0]
        for child in node.children:
            if self.enlargement(child.mbr, rect) < self.enlargement(best_child.mbr, rect):
                best_child = child
        return self.choose_leaf(best_child, rect)

    def enlargement(self, mbr, rect):
        enlarged_area = (max(mbr.x_max, rect.x_max) - min(mbr.x_min, rect.x_min)) * \
                        (max(mbr.y_max, rect.y_max) - min(mbr.y_min, rect.y_min))
        return enlarged_area - self.area(mbr)

    def area(self, mbr):
        return (mbr.x_max - mbr.x_min) * (mbr.y_max - mbr.y_min)

    def adjust_tree(self, node):
        if node == self.root:
            return
        parent = self.find_parent(self.root, node)
        parent.mbr = self.union_mbr(parent.mbr, node.mbr)
        self.adjust_tree(parent)

    def find_parent(self, parent, node):
        if parent.is_leaf or node in parent.children:
            return parent
        for child in parent.children:
            result = self.find_parent(child, node)
            if result:
                return result

    def union_mbr(self, mbr1, mbr2):
        return Rectangle(min(mbr1.x_min, mbr2.x_min), max(mbr1.x_max, mbr2.x_max),
                         min(mbr1.y_min, mbr2.y_min), max(mbr1.y_max, mbr2.y_max))

    def search(self, rect):
        return self.search_recursive(self.root, rect)

    def search_recursive(self, node, rect):
        if node.is_leaf:
            return [child.mbr for child in node.children if rect.intersects(child.mbr)]
        results = []
        for child in node.children:
            if rect.intersects(child.mbr):
                results.extend(self.search_recursive(child, rect))
        return results

if __name__ == "__main__":
    rtree = RTree()
    rtree.insert(Rectangle(1, 5, 1, 5))
    rtree.insert(Rectangle(2, 6, 2, 6))
    rtree.insert(Rectangle(3, 7, 3, 7))
    print(rtree.search(Rectangle(4, 8, 4, 8)))
