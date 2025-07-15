class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        n = len(stones)

        def helper(idx, prev, dp):
            if idx >= n:
                return False

            if dp[idx][prev]!=-1:
                return dp[idx][prev]

            if idx == n-1:
                dp[idx][prev] = 1
                return 1

            k = stones[idx] - stones[prev]

            for nxt in range(idx+1, n):
                if k-1<=stones[nxt]-stones[idx]<=k+1:
                    if helper(nxt, idx, dp) == 1:
                        dp[idx][prev] = 1
                        return 1

            dp[idx][prev] = 0
            return 0

        dp = [[-1 for _ in range(n)] for _ in range(n)]
        if stones[1]!=1:
            return False
        return False if helper(1, 0, dp) == 0 else True

            