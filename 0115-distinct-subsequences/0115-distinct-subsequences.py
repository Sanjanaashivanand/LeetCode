class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = len(s)
        n = len(t)

        if len(s) < len(t):
            return 0

        def helper(i, j, dp):
            if i==m:
                if j==n:
                    return 1
                else:
                    return 0 

            if j==n:
                return 1

            if dp[i][j]!=-1:
                return dp[i][j]

            #pick
            pick = 0
            if s[i] == t[j]:
                pick = helper(i+1, j+1, dp) + helper(i+1, j, dp)
            skip = helper(i+1, j, dp)

            dp[i][j] = max(pick, skip)
            return max(pick, skip)

        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return helper(0,0, dp)
        