class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False for _ in range(n)]

        def dfs(node):
            visited[node] = True
            for nxt in adj[node]:
                if not visited[nxt]:
                    dfs(nxt)

        dfs(source)
        return visited[destination]