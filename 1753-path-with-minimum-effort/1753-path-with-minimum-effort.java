class Solution {
    class Pair{
        int[] pos;
        int effort;

        Pair(int[] pos, int effort){
            this.pos = pos;
            this.effort = effort;
        } 
    }

    public int minimumEffortPath(int[][] heights) {
        int m = heights.length;
        int n = heights[0].length;

        // Create a dis array to store the minimum effort to reach each cell
        int[][] dis = new int[m][n];

        // Initialize dis array with a large value (max effort)
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                dis[i][j] = Integer.MAX_VALUE;
            }
        }

        // Directions: right, left, up, down
        int[][] DIRECTIONS  = new int[][]{{0,1},{0,-1},{-1,0},{1,0}};

        // Min-heap priority queue to process cells in increasing effort order
        PriorityQueue<Pair> q = new PriorityQueue<>((x,y) -> x.effort - y.effort);

        // Start from the top-left corner (0,0)
        dis[0][0] = 0;
        q.add(new Pair(new int[]{0, 0}, 0));

        while(!q.isEmpty()){
            Pair curr = q.poll();
            int r = curr.pos[0];
            int c = curr.pos[1];
            int currEffort = curr.effort;

            // If we reach the bottom-right corner, return the effort
            if(r == m - 1 && c == n - 1){
                return currEffort;
            }

            // Explore all four possible directions
            for(int[] dir : DIRECTIONS){
                int nr = r + dir[0];
                int nc = c + dir[1];

                // Skip if out of bounds
                if(nr < 0 || nr >= m || nc < 0 || nc >= n){
                    continue;
                }

                // Calculate the new effort as the maximum effort between the current path and the next cell
                int newEffort = Math.max(currEffort, Math.abs(heights[r][c] - heights[nr][nc]));

                // If a path with less effort to reach (nr, nc) is found, update and add it to the queue
                if(newEffort < dis[nr][nc]){
                    dis[nr][nc] = newEffort;
                    q.offer(new Pair(new int[]{nr, nc}, newEffort));
                }
            }
        }

        return dis[m-1][n-1]; // This should not be reached since there's always a valid path
    }
}
