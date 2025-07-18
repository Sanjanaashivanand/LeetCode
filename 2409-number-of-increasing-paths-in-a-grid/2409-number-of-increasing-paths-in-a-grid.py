class Solution(object):
    def countPaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        mod = 10 ** 9 + 7
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        dp = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]

            ans = 1

            for di, dj in directions:
                prev_i, prev_j = i + di, j + dj
                if 0 <= prev_i < m and 0 <= prev_j < n and grid[prev_i][prev_j] < grid[i][j]:
                    ans += dfs(prev_i, prev_j) % mod

            dp[i][j] = ans
            return ans

        return sum(dfs(i, j) for i in range(m) for j in range(n)) % mod