class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        indexMapHeap = []

        for i, num in enumerate(nums):
            heappush(indexMapHeap, (-num, i))

        indices = set()
        while k > 0:
            top = heappop(indexMapHeap)
            indices.add(top[1])
            k-=1

        res = []
        for i in range(0, len(nums)):
            if i in indices:
                res.append(nums[i])
        
        return res

        