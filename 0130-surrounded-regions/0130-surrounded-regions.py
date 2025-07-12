class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(i, j):
            if i<0 or i>=m or j<0 or j>=n or board[i][j] == "X" or visited[i][j]:
                return

            visited[i][j] = True

            for nx, ny in [(0,-1), (-1,0), (0,1), (1,0)]:
                dfs(i+nx, j+ny)

        for i in range(0,m):
            if board[i][0] == "O" and not visited[i][0]:
                dfs(i, 0)
            if board[i][n-1] == "O" and not visited[i][n-1]:
                dfs(i, n-1)

        for j in range(0, n):
            if board[0][j] == "O" and not visited[0][j]:
                dfs(0, j)
            if board[m-1][j] == "O" and not visited[m-1][j]:
                dfs(m-1, j)

        for i in range(1,m-1):
            for j in range(1,n-1):
                if board[i][j] == "O" and not visited[i][j]:
                    board[i][j] = "X"

