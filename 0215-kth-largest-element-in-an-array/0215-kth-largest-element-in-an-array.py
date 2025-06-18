class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h = []

        for i in nums:
            heappush(h, i)
            if len(h) > k:
                heappop(h)

        return heappop(h)
