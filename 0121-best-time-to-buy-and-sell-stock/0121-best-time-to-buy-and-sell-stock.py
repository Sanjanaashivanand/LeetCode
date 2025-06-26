class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        minSoFar = prices[0]

        for i in range(1, len(prices)):
            profit = max(profit, prices[i]  - minSoFar)
            minSoFar = min(minSoFar, prices[i])

        return profit
        