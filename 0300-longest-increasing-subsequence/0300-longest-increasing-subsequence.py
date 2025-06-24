class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1 for _ in range(len(nums))]

        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)

        