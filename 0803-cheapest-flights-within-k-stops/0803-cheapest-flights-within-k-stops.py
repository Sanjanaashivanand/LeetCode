from collections import defaultdict
from heapq import heappush, heappop

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
        
        # (cost_so_far, stops, current_node)
        pq = [(0, 0, src)]
        
        # Best dictionary to prune worse paths
        best = dict()  # key = (node, stops), value = min cost

        while pq:
            cost, stops, node = heappop(pq)

            # Reached destination
            if node == dst:
                return cost

            # If already seen better for this node with same or fewer stops, skip
            if (node, stops) in best and best[(node, stops)] <= cost:
                continue

            best[(node, stops)] = cost

            # Only expand if stops are within limit
            if stops <= k:
                for neighbor, price in adj[node]:
                    heappush(pq, (cost + price, stops + 1, neighbor))

        return -1
