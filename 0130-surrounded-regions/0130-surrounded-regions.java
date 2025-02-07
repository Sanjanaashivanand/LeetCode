class Solution {
    public int[][] directions = {{0,1}, {0,-1}, {1,0}, {-1,0}};
    public int m, n;

    // DFS to mark all 'O's connected to the boundary
    public void dfs(char[][] board, int r, int c) {
        // If out of bounds or already marked, return
        if (r < 0 || r >= m || c < 0 || c >= n || board[r][c] != 'O') {
            return;
        }
        
        // Mark this cell as safe ('S')
        board[r][c] = 'S';

        // Explore all four directions
        for (int[] dir : directions) {
            int nx = r + dir[0];
            int ny = c + dir[1];

            // Recurse in all four directions
            dfs(board, nx, ny);
        }
    }

    public void solve(char[][] board) {
        this.m = board.length;
        this.n = board[0].length;

        // Traverse the boundary rows and columns and perform DFS on 'O's
        for (int i = 0; i < m; i++) {
            // Perform DFS for the first and last column
            if (board[i][0] == 'O') dfs(board, i, 0);
            if (board[i][n - 1] == 'O') dfs(board, i, n - 1);
        }

        for (int j = 0; j < n; j++) {
            // Perform DFS for the first and last row
            if (board[0][j] == 'O') dfs(board, 0, j);
            if (board[m - 1][j] == 'O') dfs(board, m - 1, j);
        }

        // Traverse the entire grid and update the board:
        // 1. Change all 'O's to 'X' (those are surrounded by 'X')
        // 2. Change all 'S's back to 'O' (safe 'O's that are connected to the boundary)
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X'; // Surrounded by 'X'
                } else if (board[i][j] == 'S') {
                    board[i][j] = 'O'; // Safe 'O' connected to the boundary
                }
            }
        }
    }
}
