class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        m = len(text1)
        n = len(text2)

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                same = 0
                if text1[i] == text2[j]:
                    same = 1 + dp[i+1][j+1]
                not_same = max(dp[i+1][j], dp[i][j+1])

                dp[i][j] = max(same, not_same)

        return dp[0][0]
        