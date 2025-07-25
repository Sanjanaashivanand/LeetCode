class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = set([i for i in nums if i>0])
        if pos:
            return sum(pos)
        return max(nums)