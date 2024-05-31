class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def splay(self, root, key):
        if root is None or root.key == key:
            return root

        if root.key > key:
            if root.left is None:
                return root

            if root.left.key > key:
                root.left.left = self.splay(root.left.left, key)
                root = self.right_rotate(root)
            elif root.left.key < key:
                root.left.right = self.splay(root.left.right, key)
                if root.left.right is not None:
                    root.left = self.left_rotate(root.left)

            return self.right_rotate(root) if root.left is not None else root
        else:
            if root.right is None:
                return root

            if root.right.key > key:
                root.right.left = self.splay(root.right.left, key)
                if root.right.left is not None:
                    root.right = self.right_rotate(root.right)
            elif root.right.key < key:
                root.right.right = self.splay(root.right.right, key)
                root = self.left_rotate(root)

            return self.left_rotate(root) if root.right is not None else root

    def search(self, key):
        self.root = self.splay(self.root, key)
        return self.root

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        self.root = self.splay(self.root, key)

        if self.root.key == key:
            return

        new_node = Node(key)

        if self.root.key > key:
            new_node.right = self.root
            new_node.left = self.root.left
            self.root.left = None
        else:
            new_node.left = self.root
            new_node.right = self.root.right
            self.root.right = None

        self.root = new_node

    def pre_order(self, root):
        if root is not None:
            print(root.key, end=' ')
            self.pre_order(root.left)
            self.pre_order(root.right)

if __name__ == "__main__":
    tree = SplayTree()
    keys = [100, 50, 200, 40, 30, 20, 10]
    for key in keys:
        tree.insert(key)
    print("Preorder traversal of the modified Splay Tree is:")
    tree.pre_order(tree.root)
