class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        grid = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(0, n):
            if obstacleGrid[0][i] == 1:
                break
            grid[0][i] = 1

        for j in range(0, m):
            if obstacleGrid[j][0] == 1:
                break
            grid[j][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]

        return grid[m-1][n-1]