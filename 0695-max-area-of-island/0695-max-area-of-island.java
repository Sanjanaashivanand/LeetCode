class Solution {
    private int res = 0;

    private int dfs(int i, int j, int[][] grid){
        if(i<0 || i>=grid.length || 
            j<0 || j>=grid[0].length){
                return 0;
            }

        if(grid[i][j] == 0){
            return 0;
        }
        

        grid[i][j] = 0;

        return 1 + dfs(i+1, j, grid) + dfs(i-1, j, grid) +
            dfs(i, j+1, grid) + dfs(i, j-1, grid);

    }

    public int maxAreaOfIsland(int[][] grid) {
        for(int i=0; i<grid.length; i++){
            for(int j=0; j<grid[0].length; j++){
                if(grid[i][j]==1){
                    res = Math.max(res, dfs(i,j,grid));
                }
            }
        }

        return res;
    }
}