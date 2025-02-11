class Solution {
    private int m;
    private int n;

    // DFS function to explore the grid and mark visited land cells
    public void dfs(int[][] grid, boolean[][] visited, int i, int j) {
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == 0 || visited[i][j]) {
            return;
        }

        visited[i][j] = true;

        // Explore the four possible directions
        dfs(grid, visited, i + 1, j);  // Down
        dfs(grid, visited, i - 1, j);  // Up
        dfs(grid, visited, i, j + 1);  // Right
        dfs(grid, visited, i, j - 1);  // Left
    }

    public int numEnclaves(int[][] grid) {
        this.m = grid.length;
        this.n = grid[0].length;  // Correct way to get the number of columns
        boolean[][] visited = new boolean[m][n];

        // Perform DFS on the boundary to mark all land cells connected to the boundary
        for (int i = 0; i < m; i++) {
            if (grid[i][0] == 1 && !visited[i][0]) {  // First column
                dfs(grid, visited, i, 0);
            }
            if (grid[i][n - 1] == 1 && !visited[i][n - 1]) {  // Last column
                dfs(grid, visited, i, n - 1);
            }
        }

        for (int j = 0; j < n; j++) {
            if (grid[0][j] == 1 && !visited[0][j]) {  // First row
                dfs(grid, visited, 0, j);
            }
            if (grid[m - 1][j] == 1 && !visited[m - 1][j]) {  // Last row
                dfs(grid, visited, m - 1, j);
            }
        }

        // Now, count all land cells that are not visited (i.e., not connected to the boundary)
        int res = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1 && !visited[i][j]) {
                    res++;
                }
            }
        }

        return res;
    }
}
