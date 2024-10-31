class Solution {
    private static final int[][] DIRECTIONS = {
        {-1, 0}, {1, 0}, {0, -1}, {0, 1}
    };

    public int numIslands(char[][] grid) {
        if(grid == null || grid.length == 0) return 0;

        int res = 0;

        for(int i=0; i<grid.length; i++){
            for(int j=0; j<grid[0].length; j++){
                if(grid[i][j] == '1'){
                    res++;
                    dfs(grid, i, j);
                }
            }
        }

        return res;
    }

    private void dfs(char[][] grid, int x, int y){
        if(x<0 || x>=grid.length || y<0 || y>=grid[0].length || grid[x][y] == '0'){
                return;
        }

        grid[x][y] = '0';

        for(int[] direction : DIRECTIONS){
            int newX = x + direction[0];
            int newY = y + direction[1];
            dfs(grid, newX, newY);
        }
    }
}