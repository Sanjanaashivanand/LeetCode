class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        while self.parent[x] != x:
            #Path Compression
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x 

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False  # already connected — cycle
        self.parent[py] = px
        return True

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges) + 1
        uf = UnionFind(n)

        for fr, to in edges:
            if not uf.union(fr, to):
                return [fr, to]
        
        return []
