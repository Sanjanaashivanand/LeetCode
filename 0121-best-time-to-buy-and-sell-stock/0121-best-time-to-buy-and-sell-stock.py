class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minSoFar = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            profit = max(profit, prices[i]-minSoFar)
            minSoFar = min(minSoFar, prices[i])

        return profit