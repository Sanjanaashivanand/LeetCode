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

            for step in [k - 1, k, k + 1]:
                if step <= 0:
                    continue
                next_pos = stones[idx] + step
                if next_pos in idx_map:
                    next_idx = idx_map[next_pos]
                    if helper(next_idx, idx, dp) == 1:
                        dp[next_idx][idx] = 1
                        return 1

            dp[idx][prev] = 0
            return 0

        if stones[1]!=1:
            return False

        dp = [[-1 for _ in range(n)] for _ in range(n)]

        idx_map = {}
        for i in range(n):
            idx_map[stones[i]] = i
        
        return False if helper(1, 0, dp) == 0 else True

            