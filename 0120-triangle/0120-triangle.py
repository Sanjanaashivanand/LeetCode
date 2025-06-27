class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [[0] * len(row) for row in triangle]

        dp[-1] = triangle[-1]

        for i in range(len(triangle)-2, -1, -1):
            for j in range(0, len(triangle[i])):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]

        return dp[0][0]
        