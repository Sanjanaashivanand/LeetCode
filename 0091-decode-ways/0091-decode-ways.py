class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        def helper(idx, dp):
            if idx == n:
                return 1

            if s[idx] == '0':
                dp[idx] = 0
                return 0

            if dp[idx]!=-1:
                return dp[idx]

            count = helper(idx+1,dp)
            if idx+1 < n and  '10' <= s[idx:idx+2] <= '26':
                count += helper(idx+2,dp)

            dp[idx] = count
            return count

        dp = [-1 for _ in range(n+1)]
        return helper(0, dp)