class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_sum = 0
        maxi = float('-inf')

        for i in range(0, len(nums)):
            curr_sum += nums[i]
            maxi = max(curr_sum, maxi)
            if curr_sum < 0:
                curr_sum = 0

        return maxi