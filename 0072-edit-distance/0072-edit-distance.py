class Solution(object):
    def minDistance(self, text1, text2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        m = len(text1)
        n = len(text2)

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        dp[0][n] = len(text1)
        for i in range(1, m):
            dp[i][n] = dp[i-1][n] - 1

        dp[m][0] = len(text2)
        for i in range(1, n):
            dp[m][i] = dp[m][i-1] - 1


        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1]

                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1]) + 1

        return dp[0][0]
        
        