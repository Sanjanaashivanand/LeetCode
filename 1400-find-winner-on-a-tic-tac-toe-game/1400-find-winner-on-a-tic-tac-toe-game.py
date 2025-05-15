class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        n = 3
        board = [[0] * n for _ in range(n)]

        def RowCheck(row, player):
            for col in range(n):
                if board[row][col] != player:
                    return False
            return True
        
        def ColCheck(col, player):
            for row in range(n):
                if board[row][col] != player:
                    return False
            return True
        
        def DiagonalCheck(player):
            for row in range(n):
                if board[row][row] != player:
                    return False
            return True
        
        def AntiCheck(player):
            for row in range(n):
                if board[row][n-1-row] != player:
                    return False
            return True

        player = 1

        for move in moves:
            row, col = move
            board[row][col] = player

            if RowCheck(row, player) or ColCheck(col, player) \
                or (row==col and DiagonalCheck(player)) \
                or (row + col == n-1 and AntiCheck(player)):
                return 'A' if player==1 else 'B'

            player *= -1
        
        return 'Draw' if len(moves)==n*n else "Pending"

        

        
