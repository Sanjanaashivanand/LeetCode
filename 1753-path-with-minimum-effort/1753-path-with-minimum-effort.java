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
        int[][] dis = new int[m][n];

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                dis[i][j] = Integer.MAX_VALUE;
            }
        }

        int[][] DIRECTIONS  = new int[][]{{0,1},{0,-1},{-1,0},{1,0}};

        PriorityQueue<Pair> q = new PriorityQueue<>((x,y) -> x.effort - y.effort);
        dis[0][0] = 0;
        q.add(new Pair(new int[]{0, 0}, 0));

        while(!q.isEmpty()){
            Pair curr = q.poll();
            int r = curr.pos[0];
            int c = curr.pos[1];
            int currEffort = curr.effort;

            if(r == m - 1 && c == n - 1){
                return currEffort;
            }

            for(int[] dir : DIRECTIONS){
                int nr = r + dir[0];
                int nc = c + dir[1];

                if(nr < 0 || nr >= m || nc < 0 || nc >= n){
                    continue;
                }


                int newEffort = Math.max(currEffort, Math.abs(heights[r][c] - heights[nr][nc]));

                if(newEffort < dis[nr][nc]){
                    dis[nr][nc] = newEffort;
                    q.offer(new Pair(new int[]{nr, nc}, newEffort));
                }
            }
        }

        return dis[m-1][n-1]; 
    }
}
