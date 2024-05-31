class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        self.build(arr)

    def build(self, arr):
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def update(self, pos, value):
        pos += self.n
        self.tree[pos] = value
        while pos > 1:
            self.tree[pos >> 1] = self.tree[pos] + self.tree[pos ^ 1]
            pos >>= 1

    def query(self, l, r):
        res = 0
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                res += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                res += self.tree[r]
            l >>= 1
            r >>= 1
        return res

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    seg_tree = SegmentTree(arr)
    print("Sum of values in given range =", seg_tree.query(1, 5))
    seg_tree.update(1, 10)
    print("Updated sum of values in given range =", seg_tree.query(1, 5))
