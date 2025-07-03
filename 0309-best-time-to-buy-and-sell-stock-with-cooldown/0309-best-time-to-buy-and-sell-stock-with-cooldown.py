class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        self.res = -1

        def choose(idx, haveStock, profit):
            if idx >= n:
                self.res = max(self.res, profit)
                return 

            #buy
            pick = skip = 0
            if haveStock == 0:
                pick = max(choose(idx+1, 1, profit-prices[idx]), choose(idx+1, 0, profit))

            else:
                skip = max(choose(idx+2, 0, profit+prices[idx]), choose(idx+1, 1, profit))

            return max(skip, pick)

        # choose(0, 0, 0)
        # 

        dp = [[-1 for _ in range(n+1)] for _ in range(2)]

        dp[0][n] = 0
        dp[1][n] = 0

        for i in range(n-1, -1, -1):

            #Buy = 0 -> buy or not buy
            dp[0][i] = max(dp[1][i+1]-prices[i], dp[0][i+1])

            #Sell
            dp[1][i] = max(dp[0][min(i+2, n)]+prices[i], dp[1][i+1])   


        return dp[0][0]


        