class Node:
    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right

def kdtree(point_list, depth=0):
    if not point_list:
        return None
    k = len(point_list[0])
    axis = depth % k
    point_list.sort(key=lambda point: point[axis])
    median = len(point_list) // 2
    return Node(
        point=point_list[median],
        left=kdtree(point_list[:median], depth + 1),
        right=kdtree(point_list[median + 1:], depth + 1)
    )

def preorder(node):
    if not node:
        return
    print(node.point)
    preorder(node.left)
    preorder(node.right)

if __name__ == "__main__":
    points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
    root = kdtree(points)
    preorder(root)
