class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        def choose(bought, idx, dp):
            if idx == len(prices):
                return 0

            if dp[bought][idx]!=-1:
                return dp[bought][idx]

            if bought==0:
                # Choice: Buy now OR skip
                buy_now = -prices[idx] + choose(1, idx + 1, dp) 
                skip = choose(0, idx + 1, dp)
                dp[bought][idx] = max(buy_now, skip)
                return dp[bought][idx]
            else:
                # Choice: Sell now OR hold
                sell_now = prices[idx] - fee + choose(0, idx + 1, dp) 
                hold = choose(1, idx + 1, dp)
                dp[bought][idx] = max(sell_now, hold)
                return dp[bought][idx]

        dp = [[-1 for _ in range(len(prices))] for _ in range(2)]
        return choose(0, 0, dp)

            

            

        
       
        
            
