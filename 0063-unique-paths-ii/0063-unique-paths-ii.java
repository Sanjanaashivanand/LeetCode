class Solution {
    public int uniquePathsWithObstacles(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] dp = new int[m][n];

        // If the starting point is an obstacle, return 0
        if(grid[0][0] == 1) {
            return 0;
        }

        // Initialize the first row
        for(int i = 0; i < n; i++) {
            if(grid[0][i] == 1) break;  // Stop if obstacle is encountered
            dp[0][i] = 1;
        }

        // Initialize the first column
        for(int i = 0; i < m; i++) {
            if(grid[i][0] == 1) break;  // Stop if obstacle is encountered
            dp[i][0] = 1;
        }

        // Fill the dp array for the rest of the grid
        for(int i = 1; i < m; i++) {
            for(int j = 1; j < n; j++) {
                if(grid[i][j] == 0) {  // If no obstacle
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];  // Sum of paths from top and left
                } else {
                    dp[i][j] = 0;  // If obstacle, no paths
                }
            }
        }

        // The bottom-right cell contains the result
        return dp[m-1][n-1];
    }
}
