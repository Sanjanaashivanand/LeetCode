class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def choose(idx, dp):
            if idx >= len(nums):
                return 0

            if dp[idx] != -1:
                return dp[idx]

            # Pick: take current value and jump to idx+2
            pick = nums[idx] + choose(idx + 2, dp)

            # Not Pick: skip to next
            not_pick = choose(idx + 1, dp)

            dp[idx] = max(pick, not_pick)
            return dp[idx]
        
        dp = [-1] * len(nums)
        return choose(0, dp)
        