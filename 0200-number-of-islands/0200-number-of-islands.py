class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]=='0':
                return

            grid[i][j] = '0'

            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                dfs(i + dx, j + dy)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count+=1
                    dfs(i,j)

        return count
