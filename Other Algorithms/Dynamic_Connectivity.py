class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1

if __name__ == "__main__":
    uf = UnionFind(10)
    uf.union(1, 2)
    uf.union(3, 4)
    uf.union(2, 4)
    print(f"1 and 4 connected: {uf.find(1) == uf.find(4)}")
    print(f"1 and 5 connected: {uf.find(1) == uf.find(5)}")
