class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n==0:
            return 0 
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        def rob_linear(houses):
            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            for i in range(2, len(houses)):
                dp[i] = max(houses[i] + dp[i-2], dp[i-1])
            return dp[-1]

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))