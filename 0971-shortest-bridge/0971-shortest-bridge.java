class Solution {
    int[][] DIRECTIONS = new int[][]{{0,1}, {1,0}, {-1,0}, {0,-1}};
    int m, n;
    int[][] grid;

    public void dfs(int r, int c, Queue<int[]> q, boolean[][] vis){
        if(r<0 || r>=m || c<0 || c>=n || grid[r][c]==0 || vis[r][c]) return;
        vis[r][c] = true;
        q.offer(new int[]{r, c});
        for(int[] dir : DIRECTIONS){
            dfs(r + dir[0], c + dir[1], q, vis);
        }
    }

    public int shortestBridge(int[][] grid) {
        this.m = grid.length;
        this.n = grid[0].length;
        this.grid = grid;

        Queue<int[]> q = new LinkedList<>();
        boolean[][] vis = new boolean[m][n];

        // Step 1: Find first island and DFS to mark it
        boolean found = false;
        for(int i = 0; i < m && !found; i++){
            for(int j = 0; j < n && !found; j++){
                if(grid[i][j] == 1){
                    dfs(i, j, q, vis);
                    found = true;
                }
            }
        }

        // Step 2: BFS from all marked cells
        int steps = 0;
        while(!q.isEmpty()){
            int size = q.size();
            while(size-- > 0){
                int[] curr = q.poll();
                int r = curr[0], c = curr[1];
                for(int[] dir : DIRECTIONS){
                    int nr = r + dir[0], nc = c + dir[1];
                    if(nr < 0 || nr >= m || nc < 0 || nc >= n || vis[nr][nc]) continue;

                    if(grid[nr][nc] == 1) return steps; // Found second island

                    q.offer(new int[]{nr, nc});
                    vis[nr][nc] = true;
                }
            }
            steps++;
        }

        return -1; // Shouldn't happen
    }
}
