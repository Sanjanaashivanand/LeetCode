class Solution {
    private int n, m;
    private int[][] matrix;
    private int[][] DIRECTIONS = {{0,1}, {1,0}, {-1,0}, {0,-1}};

    public int dfs(int i, int j, int[][] dp){
        if(i<0 || i>=m || j<0 || j>=n ) return 0;

        if(dp[i][j] != 0) return dp[i][j];

        int currentMax = 1;

        for(int[] dir:DIRECTIONS){
            int x = i + dir[0];
            int y = j + dir[1];

            if(x>=0 && y>=0 && x<m && y<n && this.matrix[i][j] < this.matrix[x][y]){
                currentMax = Math.max(currentMax, 1 + dfs(x, y, dp));
            }
        }

        dp[i][j] = currentMax;
        return currentMax;
    }

    public int longestIncreasingPath(int[][] matrix) {
        this.m = matrix.length;
        this.n = matrix[0].length;
        this.matrix = matrix;
        int[][] dp = new int[m][n];

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                dfs(i, j, dp);
            }
        }

        int res = -1;
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                res = Math.max(res, dp[i][j]);
            }
        }

        return res;
    }
}