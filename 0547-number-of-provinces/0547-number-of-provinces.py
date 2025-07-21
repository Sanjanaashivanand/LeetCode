class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        m = len(isConnected)
        n = len(isConnected[0])

        adj = defaultdict(list)

        for i in range(m):
            for j in range(n):
                if isConnected[i][j] == 1:
                    adj[i].append(j)
                    adj[j].append(i)

        nodes = len(adj)
        visited = [False for _ in range(nodes)]

        def dfs(node):
            visited[node] = True

            for nxt in adj[node]:
                if not visited[nxt]:
                    dfs(nxt)

        count = 0
        for key in adj:
            if not visited[key]:
                dfs(key)
                count+=1

        return count 
