import numbers
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        adj = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    adj[i].append(j)
                    adj[j].append(i)

        vis = [False] * len(adj)
        res = 0

        for i in range(n):
            if not vis[i]:
                res+=1
                self.dfs(i, adj, vis)

        return res
        
    def dfs(self, i, adj, vis):
        vis[i] = True

        for next_i in adj[i]:
            if not vis[next_i]:
                self.dfs(next_i, adj, vis)
        
