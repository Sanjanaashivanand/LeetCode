class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]

        n = len(nums)+1
        dp = [-1 for _ in range(len(nums)+1)]
        dp[n-1] = 0

        for i in range(n-2, -1, -1):
            dp[i] = max(nums[i] + dp[min(i+2, n-1)], dp[i+1])

        return dp[0]