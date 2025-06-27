class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(0, n):
            dp[0][i] = matrix[0][i]

        for i in range(1, n):
            for j in range(0, n):
                if j == 0:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + matrix[i][j]

                elif j == n-1:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + matrix[i][j]

                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1]) + matrix[i][j]
        print(dp)
        res = float('inf')
        for i in range(0, n):
            res = min(dp[n-1][i], res)

        return res
