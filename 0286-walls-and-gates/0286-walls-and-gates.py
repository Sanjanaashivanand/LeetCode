class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])

        q = deque()

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))

        while q:
            size = len(q)

            for _ in range(0, size):
                #Current (row, col)
                r, c = q.popleft()

                for dx, dy in [(0,-1), (-1,0), (1,0), (0,1)]:
                    nr = r + dx
                    nc = c + dy

                    if nr<0 or nr>=m or nc<0 or nc>=n or rooms[nr][nc]==0:
                        continue

                    if rooms[r][c] + 1 < rooms[nr][nc]:
                        rooms[nr][nc] = rooms[r][c] + 1
                        q.append((nr, nc))


        