class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = len(board)

        board_set = set()

        for i in range(0, 9):
            for j in range(0,9):
                if board[i][j]!=".":
                    key_row = board[i][j] + " in row " + str(i) 
                    key_col = board[i][j] +  " in col " + str(j) 
                    key_box = board[i][j] + " in box " + str(i//3) + " " + str(j//3)

                    if key_row in board_set:
                        return False
                    
                    if key_col in board_set:
                        return False

                    if key_box in board_set:
                        return False

                    board_set.add(key_row)
                    board_set.add(key_col)
                    board_set.add(key_box)

        return True