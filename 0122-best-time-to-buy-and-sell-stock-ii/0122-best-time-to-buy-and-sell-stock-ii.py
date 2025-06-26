class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)

        # def dfs(idx, profit, haveStock):
        #     if idx == n:
        #         return profit

        #     #Buy
        #     buy = sell = 0
        #     if haveStock == False:
        #         buy = max(dfs(idx+1, profit-prices[idx], True), dfs(idx+1, profit, False))

        #     #Sell
        #     else:
        #         sell = max(dfs(idx+1, profit+prices[idx], False), dfs(idx+1, profit, True))

        #     return max(buy, sell)

        dp = [[-1] * 2] * (n+1)
        dp[n][0] = 0
        dp[n][1] = 0

        for i in range(n-1, -1, -1):
            #Sell
            profit = max(prices[i]+dp[i+1][1], dp[i+1][0])
            dp[i][0] = profit

            #Buy
            profit = max(-prices[i]+dp[i+1][0], dp[i+1][1])
            dp[i][1] = profit

        return dp[0][1]

