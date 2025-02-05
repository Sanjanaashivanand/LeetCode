class Solution {
    public int orangesRotting(int[][] grid) {
        int n = grid.length; 
        int m = grid[0].length;

        Queue<int[]> q = new LinkedList<>();
        boolean[][] visited = new boolean[n][m];

        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(grid[i][j] == 2){
                    q.add(new int[]{i, j});
                    visited[i][j] = true;
                }
            }
        }

        int count = -1;
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        while(!q.isEmpty()){
            int size = q.size();
            count++;

            for(int i=0; i<size; i++){
                int[] cell = q.poll();
                int row = cell[0];
                int col = cell[1];

                for(int[] dir: directions){
                    int nx = row+dir[0];
                    int ny = col+dir[1];

                    if (nx >= 0 && nx < n && ny >= 0 && ny < m 
                        && !visited[nx][ny] && grid[nx][ny] == 1) {
                        visited[nx][ny] = true;
                        grid[nx][ny] = 2;  
                        q.add(new int[]{nx, ny});
                    }
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 1) {
                    return -1; 
                }
            }
        }

        return count == -1 ? 0 : count;

    }
}