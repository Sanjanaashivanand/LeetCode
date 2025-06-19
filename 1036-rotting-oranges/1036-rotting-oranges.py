class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        q = deque()
        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i,j])
                    visited[i][j] = True

        directions = [[0,1], [0,-1], [-1,0], [1,0]]
        count = -1

        while q:
            size = len(q)
            count+=1

            for i in range(size):
                row, col = q.popleft()

                for dr,dc in directions:
                    r = row + dr
                    c = col + dc

                    if 0<=r<m and 0<=c<n and grid[r][c]==1 and not visited[r][c]:
                        q.append([r,c])
                        grid[r][c] = 2
                        visited[r][c] = True

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return 0 if count == -1 else count



        