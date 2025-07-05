class Solution(object):
    def findMaxForm(self, strs, m, n):
        length = len(strs)
        dp = {}

        def dfs(idx, m, n):
            if idx == length:
                return 0

            if (idx, m, n) in dp:
                return dp[(idx, m, n)]

            zeros = strs[idx].count('0')
            ones = strs[idx].count('1')

            pick = 0
            if m - zeros >= 0 and n - ones >= 0:
                pick = 1 + dfs(idx + 1, m - zeros, n - ones)

            not_pick = dfs(idx + 1, m, n)

            dp[(idx, m, n)] = max(pick, not_pick)
            return dp[(idx, m, n)]

        return dfs(0, m, n)
