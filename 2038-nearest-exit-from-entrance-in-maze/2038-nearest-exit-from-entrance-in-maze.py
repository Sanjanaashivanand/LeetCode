class Solution(object):
    def nearestExit(self, maze, entrance):
        m = len(maze)
        n = len(maze[0])
        
        dis = [[float('inf') for _ in range(n)] for _ in range(m)]

        q = deque()
        direction = [[0,1], [0,-1], [-1,0], [1,0]]
        q.append(entrance)
        dis[entrance[0]][entrance[1]] = 0
        maze[entrance[0]][entrance[1]] = '+'

        while q:
            row, col = q.popleft()

            for dr, dc in direction:
                r = row + dr
                c = col + dc

                if 0 <= r < m and 0 <= c < n and maze[r][c] == '.':
                    dis[r][c] = dis[row][col] + 1
                    maze[r][c] = '+'  # mark as visited
                    q.append([r, c])

        res = float('inf')

        for i in range(n):
            if dis[0][i] != float('inf') and [0, i] != entrance:
                res = min(res, dis[0][i])
            if dis[m-1][i] != float('inf') and [m-1, i] != entrance:
                res = min(res, dis[m-1][i])

        for i in range(m):
            if dis[i][0] != float('inf') and [i, 0] != entrance:
                res = min(res, dis[i][0])
            if dis[i][n-1] != float('inf') and [i, n-1] != entrance:
                res = min(res, dis[i][n-1])

        return res if res != float('inf') else -1

        