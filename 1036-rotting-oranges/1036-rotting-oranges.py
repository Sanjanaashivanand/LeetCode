class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        q = deque()
        n_oranges = 0

        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    n_oranges += 1
                
        
        if n_oranges == 0:
            return 0
            
        count = 0
        rotten = 0

        while q:
            size = len(q)
            count+=1

            for _ in range(0, size):
                i, j = q.popleft()

                for nx, ny in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nr = i + nx
                    nc = j + ny

                    if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] == 0:
                        continue

                    if grid[nr][nc] == 1:
                        rotten+=1
                        grid[nr][nc] = 2
                        q.append((nr,nc))

        if rotten==n_oranges:
            return count-1
        return -1