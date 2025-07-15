class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        def helper(total, dp):
            if total == 0:
                return 0
            if total < 0:
                return float('inf')
            
            if dp[total]!=-1:
                return dp[total]

            mini = float('inf')
            for coin in coins:
                if coin <= total:
                    coins_needed = 1 + helper(total - coin, dp)
                    mini = min(mini, coins_needed)

            dp[total] = mini
            return mini
            
        dp = [-1 for _ in range(amount+1)]
        res = helper(amount, dp)
        return res if res!=float('inf') else -1