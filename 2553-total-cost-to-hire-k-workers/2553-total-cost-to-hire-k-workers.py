class Solution(object):
    import heapq

    def totalCost(self, costs, k, candidates):
        n = len(costs)
        cost = 0

        left = 0
        right = n - 1

        left_heap = []
        right_heap = []

        # Preload up to 'candidates' from both sides
        while len(left_heap) < candidates and left <= right:
            heapq.heappush(left_heap, costs[left])
            left += 1
        while len(right_heap) < candidates and left <= right:
            heapq.heappush(right_heap, costs[right])
            right -= 1

        for _ in range(k):
            # Always hire the cheaper candidate
            if not right_heap or (left_heap and left_heap[0] <= right_heap[0]):
                cost += heapq.heappop(left_heap)
                if left <= right:
                    heapq.heappush(left_heap, costs[left])
                    left += 1
            else:
                cost += heapq.heappop(right_heap)
                if left <= right:
                    heapq.heappush(right_heap, costs[right])
                    right -= 1

        return cost