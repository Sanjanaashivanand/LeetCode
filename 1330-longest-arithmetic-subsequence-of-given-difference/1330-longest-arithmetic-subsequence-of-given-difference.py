class Solution(object):
    def longestSubsequence(self, nums, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        n = len(nums)
        dp = {}
        res = 0

        for num in nums:
            if num - difference in dp:
                dp[num] = dp[num-difference] + 1
            else:
                dp[num] = 1

            res = max(res, dp[num])
            
        return res

        