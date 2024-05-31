class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= index & -index
        return sum

    def range_query(self, left, right):
        return self.query(right) - self.query(left - 1)

if __name__ == "__main__":
    arr = [1, 7, 3, 0, 7, 8, 3, 2, 6, 2]
    fenwick_tree = FenwickTree(len(arr))
    for i, val in enumerate(arr):
        fenwick_tree.update(i + 1, val)
    print("Sum of elements in arr[1:5] =", fenwick_tree.range_query(1, 5))
    fenwick_tree.update(3, 6)
    print("Updated sum of elements in arr[1:5] =", fenwick_tree.range_query(1, 5))
