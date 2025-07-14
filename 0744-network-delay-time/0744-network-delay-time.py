from heapq import heappush, heappop
from collections import defaultdict

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        heap = [(0, k)]  # (distance, node)
        visited = set()
        res = 0

        while heap:
            curr_dis, curr_node = heappop(heap)
            if curr_node in visited:
                continue
            visited.add(curr_node)
            res = max(res, curr_dis)

            for neighbor, weight in adj[curr_node]:
                if neighbor not in visited:
                    heappush(heap, (curr_dis + weight, neighbor))

        return res if len(visited) == n else -1
