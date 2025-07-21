class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x]!=x:
            self.parent[x] = self.find(self.parent[x])
            x = self.parent[x]
        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False

        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootX] = rootY
            self.rank[rootX] += 1
        return True

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges) + 1
        uf = UnionFind(n)
        res = []

        for u, v in edges:
            if not uf.union(u, v):
                res = [u, v]
                break

        return res
            
