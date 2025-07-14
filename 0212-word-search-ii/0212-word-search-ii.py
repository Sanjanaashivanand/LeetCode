class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.word = None  # \U0001f195 store full word here


class Solution(object):
    def findWords(self, board, words):
        m = len(board)
        n = len(board[0])
        res = set()
        self.root = TrieNode()

        def dfs(r, c, visited, curr):
            char = board[r][c]
            if char not in curr.children:
                return

            visited[r][c] = True
            curr = curr.children[char]

            if curr.endOfWord:
                res.add(curr.word)
                curr.endOfWord = False  # avoid duplicates

            for dx, dy in [[0,1], [1,0], [-1,0], [0,-1]]:
                nr = r + dx
                nc = c + dy

                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    dfs(nr, nc, visited, curr)

            visited[r][c] = False  # \U0001f501 backtrack

        # Build the Trie
        for word in words:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.endOfWord = True
            curr.word = word  # \U0001f195 store the word directly

        # Start DFS
        for i in range(m):
            for j in range(n):
                if board[i][j] in self.root.children:
                    visited = [[False for _ in range(n)] for _ in range(m)]
                    dfs(i, j, visited, self.root)

        return list(res)
