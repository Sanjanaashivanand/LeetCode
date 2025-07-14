class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []

        for x, y in points:
            dis = -(x**2 + y**2)  # negate for max-heap
            if len(heap) < k:
                heapq.heappush(heap, (dis, x, y))
            else:
                heapq.heappushpop(heap, (dis, x, y))  # efficient replace

        return [[x, y] for (_, x, y) in heap]