class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        n_ele = n // 3
        range_point = 2 * n_ele

    
        left_sum = [0] * n
        max_heap = []
        curr_sum = 0

        for i in range(n):
            heappush(max_heap, -nums[i])
            curr_sum += nums[i]

            if len(max_heap) > n_ele:
                curr_sum += heappop(max_heap)  

            if len(max_heap) == n_ele:
                left_sum[i] = curr_sum

        right_sum = [0] * n
        min_heap = []
        curr_sum = 0

        for i in range(n-1, -1, -1):
            heappush(min_heap, nums[i])
            curr_sum += nums[i]

            if len(min_heap) > n_ele:
                curr_sum -= heappop(min_heap)

            if len(min_heap) == n_ele:
                right_sum[i] = curr_sum

        res = float('inf')
        for i in range(n_ele - 1, range_point):
            res = min(res, left_sum[i] - right_sum[i + 1])

        return res
