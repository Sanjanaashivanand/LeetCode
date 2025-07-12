class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def dfs(node):
            vis[node] = True

            for next in adj[node]:
                if not vis[next]:
                    dfs(next)
        
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        count = 0
        vis = [False] * n

        for i in range(n):
            if not vis[i]:
                dfs(i)
                count+=1

        return count
        