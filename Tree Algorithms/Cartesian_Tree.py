class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def build_cartesian_tree(arr):
    if not arr:
        return None

    min_index = arr.index(min(arr))
    root = Node(arr[min_index])
    root.left = build_cartesian_tree(arr[:min_index])
    root.right = build_cartesian_tree(arr[min_index + 1:])
    return root

def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.key, end=" ")
        inorder_traversal(root.right)

if __name__ == "__main__":
    arr = [3, 2, 6, 1, 9]
    root = build_cartesian_tree(arr)
    print("Inorder traversal of the constructed Cartesian Tree is:")
    inorder_traversal(root)
