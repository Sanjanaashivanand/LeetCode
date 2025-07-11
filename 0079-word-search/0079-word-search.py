class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]
        
        def dfs(i, j, char_idx):
            if char_idx == len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if visited[i][j] or board[i][j] != word[char_idx]:
                return False

            visited[i][j] = True

            for dx, dy in [[0,1], [1,0], [-1,0], [0,-1]]:
                r = i + dx 
                c = j + dy

                if dfs(r, c, char_idx+1):
                    return True

            visited[i][j] = False
            return False

        for i in range(0, m):
            for j in range(0, n):
                if dfs(i, j, 0):
                    return True

        return False