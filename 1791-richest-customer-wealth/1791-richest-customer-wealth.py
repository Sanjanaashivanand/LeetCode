class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxSum = -1
        max = -1

        for acc in range(0, len(accounts)):
            sum = 0
            for i in accounts[acc]:
                sum += i
            
            if sum > maxSum:
                maxSum = sum
                max = acc

        return maxSum

        