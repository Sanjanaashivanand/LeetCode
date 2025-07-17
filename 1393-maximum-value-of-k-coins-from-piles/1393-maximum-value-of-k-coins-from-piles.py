class Solution(object):
    def maxValueOfCoins(self, piles, k):
        n = len(piles)
        dp = [0] * (k + 1)  # dp[j] = max sum using j coins so far

        for pile in piles:
            # Build prefix sum of the current pile
            prefix = [0]
            for coin in pile:
                prefix.append(prefix[-1] + coin)

            # New dp array to store updates for this pile
            new_dp = dp[:]

            # Try taking x coins from current pile
            for coins_taken in range(1, min(len(pile), k) + 1):
                for j in range(k, coins_taken - 1, -1):
                    new_dp[j] = max(new_dp[j], prefix[coins_taken] + dp[j - coins_taken])

            dp = new_dp

        return dp[k]
