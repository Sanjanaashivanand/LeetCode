from collections import deque

class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        res = [[float('inf')] * n for _ in range(m)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    q.append((i, j))

        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if res[nx][ny] > res[x][y] + 1:
                        res[nx][ny] = res[x][y] + 1
                        q.append((nx, ny))

        return res
