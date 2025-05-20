class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxSum = -1

        for acc in accounts:
            maxSum = max(maxSum, sum(acc))
        
        return maxSum

        