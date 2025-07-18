class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)

        def helper(idx, k, bought):
            if idx==n or k==0:
                return 0
            if (idx, k, bought) in dp:
                return dp[(idx, k, bought)]

            buy = sell = 0
            if not bought:
                buy = max(-prices[idx] + helper(idx+1, k, True), helper(idx+1, k, False))
            else:
                sell = max(prices[idx] + helper(idx+1, k-1, False), helper(idx+1, k, True))

            dp[(idx, k, bought)] = max(buy, sell)
            return max(buy, sell)

        dp = {}
        return helper(0, k, False)