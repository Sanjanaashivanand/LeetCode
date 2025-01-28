class Solution {
    private int m;
    private int n;

    public int dfs(int[][] grid, int i, int j){
        if(i<0 || i>=m || j<0 || j>=n || grid[i][j]==0){
            return 0;
        }

        int count = grid[i][j];
        grid[i][j] = 0;
        count += dfs(grid, i+1, j);
        count += dfs(grid, i-1, j);
        count += dfs(grid, i, j-1);
        count += dfs(grid, i, j+1);

        return count;
    }

    public int findMaxFish(int[][] grid) {
        this.m = grid.length;
        this.n = grid[0].length;
        int res = 0;

        for(int i=0;i<m; i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]>0){
                    res = Math.max(dfs(grid, i, j),res);
                }
            }
        }

        return res;
        
    }
}