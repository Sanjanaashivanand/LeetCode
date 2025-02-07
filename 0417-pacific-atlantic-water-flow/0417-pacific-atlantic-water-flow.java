class Solution {
    private int[][] DIRECTIONS = {{0,1}, {0,-1}, {1,0}, {-1,0}};

    public void dfs(int[][] heights, boolean[][] ocean, int r, int c){
        int n = heights.length;
        int m = heights[0].length;
        ocean[r][c] = true;
        
        for(int[] dir: DIRECTIONS){
            int nr = r + dir[0];
            int nc = c + dir[1];

            if(nr>=0 && nr<n && nc>=0 && nc<m && !ocean[nr][nc] && heights[nr][nc] >= heights[r][c]){
                dfs(heights, ocean, nr, nc);
            }
        }
    }

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int n = heights.length;
        int m = heights[0].length;
        List<List<Integer>> result = new ArrayList<>();
        boolean[][] pacific = new boolean[n][m];
        boolean[][] atlantic = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            dfs(heights, pacific, i, 0);
            dfs(heights, atlantic, i, m - 1);
        }

        for (int j = 0; j < m; j++) {
            dfs(heights, pacific, 0, j);
            dfs(heights, atlantic, n - 1, j);
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    result.add(Arrays.asList(i, j));
                }
            }
        }

        return result; 
    }
}