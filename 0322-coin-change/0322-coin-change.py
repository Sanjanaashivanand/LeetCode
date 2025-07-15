class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # def helper(total, dp):
        #     if total == 0:
        #         return 0
        #     if total < 0:
        #         return float('inf')
            
        #     if dp[total]!=-1:
        #         return dp[total]

        #     mini = float('inf')
        #     for coin in coins:
        #         if coin <= total:
        #             coins_needed = 1 + helper(total - coin, dp)
        #             mini = min(mini, coins_needed)

        #     dp[total] = mini
        #     return mini
            
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0

        for total in range(1, amount+1):
            mini = float('inf')
            for coin in coins:
                if coin <= total:
                    coins_needed = 1 + dp[max(0, total-coin)]
                    mini = min(mini, coins_needed)

            dp[total] = mini

        return dp[amount] if dp[amount]!=float('inf') else -1