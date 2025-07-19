class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefix = 1 if nums[0] == 1 else 0
        res = 1 if nums[0] == 1 else 0 

        for i in range(1, n):
            if nums[i] == 1:
                prefix += 1
                res = max(res, prefix)
            else:
                prefix = 0

        return res