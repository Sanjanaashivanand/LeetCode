class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        heap = [] #(dis, point)
        heapq.heappush(heap, (0,-1))
        visited = set()
        cost = 0

        while heap:
            curr_dis, curr_point = heapq.heappop(heap)
            curr_x, curr_y = points[curr_point]
            if (curr_x, curr_y) in visited:
                continue
            visited.add((curr_x, curr_y))
            cost += curr_dis

            for i in range(len(points)):
                point_x, point_y = points[i]
                if (point_x, point_y) in visited:
                    continue

                dis = abs(point_x - curr_x) + abs(point_y - curr_y)
                heapq.heappush(heap, (dis, i))

        return cost

            
