class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        adj = defaultdict(list)

        for fr, to in tickets:
            heapq.heappush(adj[fr], to)

        path = []
        def dfs(curr):
            while adj[curr]:
                dfs(heapq.heappop(adj[curr]))
            path.append(curr)
        
        dfs("JFK")
        return path[::-1]