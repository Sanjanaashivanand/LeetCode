class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = []
        i = 1

        while i * i <= n:
            squares.append(i*i)
            i+=1

        dp = [float('inf')] * (n+1)
        dp[0] = 0

        for i in range(1, n+1):
            for sq in squares:
                if sq <= i:
                    dp[i] = min(dp[i], 1 + dp[i - sq])

        return dp[n]
        