class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        n = len(days)

        # def helper(idx):
        #     if idx >= n:
        #         return 0

        #     cost = float('inf')
        #     #Day Pass
        #     cost = min(costs[0] + helper(idx + 1), cost)

        #     #7-day Pass
        #     next_pass = days[idx] + 7
        #     next_idx = idx
        #     while next_idx < n and days[next_idx] < next_pass:
        #         next_idx += 1
        #     cost = min(costs[1] + helper(next_idx), cost)

        #     #30 day Pass
        #     next_pass = days[idx] + 30
        #     next_idx = idx
        #     while next_idx < n and days[next_idx] < next_pass:
        #         next_idx += 1
        #     cost = min(costs[2] + helper(next_idx), cost)

        #     return cost

        # return helper(0)

        dp = [float('inf') for _ in range(n+1)]
        dp[n] = 0

        for i in range(n-1, -1, -1):
            cost = dp[i]

            #Day Pass
            cost = min(cost, costs[0] + dp[i+1])

            #7 day Pass
            next_idx = i
            while next_idx < n and days[next_idx] < days[i] + 7:
                next_idx += 1
            cost = min(costs[1] + dp[min(n, next_idx)], cost)

            #7 day Pass
            next_idx = i
            while next_idx < n and days[next_idx] < days[i] + 30:
                next_idx += 1
            cost = min(costs[2] + dp[min(n, next_idx)], cost)

            dp[i] = cost

        return dp[0]
    


