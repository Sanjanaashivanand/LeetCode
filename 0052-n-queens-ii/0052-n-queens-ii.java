class Solution {
    private boolean isSafe(int n, char[][] nQueens, int row, int col){
        // Check the column
        for(int i = 0; i < n; i++) {
            if(nQueens[i][col] == 'Q') {
                return false;
            }
        }

        // Check the row
        for(int j = 0; j < n; j++) {
            if(nQueens[row][j] == 'Q') {
                return false;
            }
        }

        // Check the upper-left diagonal
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if (nQueens[i][j] == 'Q') {
                return false;
            }
        }

        // Check the upper-right diagonal
        for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
            if (nQueens[i][j] == 'Q') {
                return false;
            }
        }

        return true;
    }

    private int count = 0;

    private void solveNQueens(int n, char[][] nQueens, int row) {
        if (row == n) {
            count++;  // Found a valid solution
            return;
        }

        for (int col = 0; col < n; col++) {
            if (isSafe(n, nQueens, row, col)) {
                nQueens[row][col] = 'Q';
                solveNQueens(n, nQueens, row + 1);
                nQueens[row][col] = '.';  // Backtrack
            }
        }
    }

    public int totalNQueens(int n) {
        char[][] nQueens = new char[n][n];
        
        for (int i = 0; i < n; i++) {
            Arrays.fill(nQueens[i], '.');
        }
        
        solveNQueens(n, nQueens, 0);
        return count;  // Return the total count of solutions
    }
}
