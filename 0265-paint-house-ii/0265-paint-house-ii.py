class Solution(object):
    def minCostII(self, costs):
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

            minimum = float('inf')
            for i in range(0, len(costs[0])):
                if i == prev:
                    continue

                minimum = min(minimum, costs[idx][i]+helper(i, idx+1, dp))

            dp[(prev, idx)] = minimum
            return minimum

        res = float('inf')
        dp = {}
        for i in range(0, len(costs[0])):
            res = min(res, helper(i, 0, dp))
        
        return res