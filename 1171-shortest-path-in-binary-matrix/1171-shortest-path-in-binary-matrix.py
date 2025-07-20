class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        res = [[float('inf')] * n for _ in range(n)]
        if grid[0][0] == 1:
            return -1
        q = deque()
        q.append((0,0))
        res[0][0] = 1
        directions = [(0,1), (1,0), (-1,0), (0,-1), (-1,-1), (1,1), (1, -1), (-1,1)]

        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if grid[nx][ny]==0 and res[nx][ny] > res[x][y] + 1:
                        res[nx][ny] = res[x][y] + 1
                        q.append((nx, ny))

        print(res)
        return res[n-1][n-1] if res[n-1][n-1] != float('inf') else -1
        