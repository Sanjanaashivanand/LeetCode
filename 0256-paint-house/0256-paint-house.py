class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)

        def helper(prev, idx, dp):
            if idx == n:
                return 0 

            if (prev, idx) in dp:
                return dp[(prev, idx)]

            #Pick Blue
            blue = float('inf')
            if prev!=0:
                blue = costs[idx][0] + helper(0, idx+1, dp)
            #Pick Red
            red = float('inf')
            if prev!=1:
                red = costs[idx][1] + helper(1, idx+1, dp)
            #Pick Green
            green = float('inf')
            if prev!=2:
                green = costs[idx][2] + helper(2, idx+1, dp)

            dp[(prev, idx)] = min(red, green, blue)
            return min(red, green, blue)

        res = float('inf')
        dp = {}
        for i in range(0, 3):
            res = min(res, helper(i, 0, dp))
        
        return res
        