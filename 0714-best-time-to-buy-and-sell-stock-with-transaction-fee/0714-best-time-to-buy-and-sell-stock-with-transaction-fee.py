class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        n = len(prices)
        dp = [[-1 for _ in range(n+1)] for _ in range(2)]

        dp[0][n] = 0
        dp[1][n] = 0

        for i in range(n-1, -1, -1):

            #Buy = 0 -> buy or not buy
            dp[0][i] = max(dp[1][i+1]-prices[i], dp[0][i+1])

            #Sell
            dp[1][i] = max(dp[0][i+1]+prices[i]-fee, dp[1][i+1])   


        return dp[0][0]

            

            

        
       
        
            
