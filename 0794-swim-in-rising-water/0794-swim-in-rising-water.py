from os import curdir
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)
        m = len(grid[0])

        q = []
        heappush(q, (grid[0][0],0,0))
        visited = set()

        while q:
            curr_t, curr_x, curr_y = heappop(q)

            if (curr_x, curr_y) in visited:
                continue

            if curr_x == m-1 and curr_y == n-1:
                return curr_t

            visited.add((curr_x, curr_y))
            print(grid[curr_x][curr_y])
            
            for dx, dy in [[0,-1], [1,0], [-1, 0], [0, 1]]:
                nx = curr_x + dx 
                ny = curr_y + dy 

                if 0<=nx<m and 0<=ny<n:
                    new_time = max(curr_t, grid[nx][ny])
                    heappush(q, (new_time, nx, ny))

        return -1
