class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n = len(coins)
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for curr in range(1, amount+1):
            for coin in coins:
                if coin <= curr:
                    dp[curr] = min(dp[curr], 1+dp[curr - coin])

        return dp[amount] if dp[amount] != float('inf') else -1