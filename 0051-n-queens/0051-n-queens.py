class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        board = [["."] * n for _ in range(n)]

        def create_board(state):
            board = []
            for row in state:
                board.append("".join(row))
            return board

        def backtrack(row, diagonals, anti_diagonals, cols, board_state):
            if row == n:
                res.append(create_board(board_state))
                return

            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col

                if (col in cols) or \
                    (curr_diagonal in diagonals) or \
                    (curr_anti_diagonal in anti_diagonals):
                    continue

                else:
                    cols.add(col)
                    diagonals.add(curr_diagonal)
                    anti_diagonals.add(curr_anti_diagonal)
                    board_state[row][col] = 'Q'

                    backtrack(row+1, diagonals, anti_diagonals, cols, board_state)

                    cols.remove(col)
                    diagonals.remove(curr_diagonal)
                    anti_diagonals.remove(curr_anti_diagonal)
                    board_state[row][col] = '.'


        backtrack(0, set(), set(), set(), board)
        return res