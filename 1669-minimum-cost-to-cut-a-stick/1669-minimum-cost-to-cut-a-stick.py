class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        cuts.append(0)
        cuts.append(n)
        cuts.sort()

        dp = {}
        
        def helper(left, right, dp):
            if left > right:
                return 0    

            if (left, right) in dp:
                return dp[(left, right)]

            mini = float('inf')

            for i in range(left, right+1):
                cost = cuts[right+1] - cuts[left-1] + helper(left, i-1, dp) + helper(i+1, right, dp)
                mini = min(mini, cost)
            
            dp[(left,right)] = mini
            return mini

        return helper(1, len(cuts)-2, dp)
        