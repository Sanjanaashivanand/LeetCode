class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n = len(coins)

        def helper(idx, curr, dp):
            if idx == 0:
                if curr%coins[0] == 0:
                    return curr/coins[idx]
                else:
                    return float('inf')

            if (idx, curr) in dp:
                return dp[(idx, curr)]

            #Pick
            pick = float('inf')
            if coins[idx] <= curr:
                pick = 1 + helper(idx, curr - coins[idx], dp)

            skip = helper(idx-1, curr, dp)

            dp[(idx, curr)] = min(pick, skip)
            return dp[(idx,curr)]


        dp = {}
        res = helper(len(coins)-1, amount, dp) 
        return res if res < float('inf') else -1

            
        