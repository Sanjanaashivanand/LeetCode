class Solution(object):
    def longestArithSeqLength(self, nums):
        n = len(nums)
        max_len = 0
        dp = [{} for _ in range(n)]  # dp[i][diff] = length of seq ending at i with diff

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                # Extend sequence from j to i, or start fresh at j
                dp[i][diff] = dp[j].get(diff, 1) + 1
                max_len = max(max_len, dp[i][diff])

        return max_len
