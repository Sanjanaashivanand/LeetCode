class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        def dfs(node, parent):
            vis[node] = True

            for next in adj[node]:
                if not vis[next]:
                    if dfs(next, node):
                        return True 
                elif next != parent:
                    return True

            return False
        
        if len(edges) != n - 1:
            return False

        adj = {}
        for i in range(n):
            adj[i] = []
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        
        vis = [False] * n

        for i in range(0, n):
            if not vis[i]:
                if dfs(i, -1):
                    return False

        return True