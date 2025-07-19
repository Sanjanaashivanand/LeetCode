class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefix = [0] * (n)
        prefix[0] = 1 if nums[0] == 1 else 0 

        for i in range(1, n):
            if nums[i] == 1:
                prefix[i] = prefix[i-1] + 1

        return max(prefix)