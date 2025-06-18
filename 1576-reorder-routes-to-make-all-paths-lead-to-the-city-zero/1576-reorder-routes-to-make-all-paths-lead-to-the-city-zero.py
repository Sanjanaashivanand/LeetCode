class Solution(object):

    def dfs(self, i, routes, vis, adj):
        vis[i] = True

        for next_i in adj[i]:
            if not vis[next_i]:
                if (i, next_i) in routes:
                    self.res += 1
                self.dfs(next_i, routes, vis, adj)
                

    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        routes = set()
        adj = [[] for _ in range(n)]
        self.res = 0

        for edge in connections:
            routes.add((edge[0], edge[1]))
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        visited = [False] * n
        
        self.dfs(0, routes, visited, adj)

        return self.res
