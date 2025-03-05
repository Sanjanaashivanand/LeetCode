class Solution {
    public int minPathSum(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] dp = new int[m][n];

        dp[0][0] = grid[0][0];

        // Initialize the first row
        for(int i = 1; i < n; i++) {
            dp[0][i] = dp[0][i-1] + grid[0][i];
        }

        // Initialize the first column
        for(int i = 1; i < m; i++) {
            dp[i][0] = dp[i-1][0] + grid[i][0];
        }

        // Fill the dp array for the rest of the grid
        for(int i = 1; i < m; i++) {
            for(int j = 1; j < n; j++) {
                dp[i][j] = Math.min(grid[i][j] + dp[i-1][j], grid[i][j] + dp[i][j-1]); 
            }
        }

        // The bottom-right cell contains the result
        return dp[m-1][n-1];
    }
}