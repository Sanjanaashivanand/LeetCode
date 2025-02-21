class Solution {
    public int nearestExit(char[][] maze, int[] entrance) {
        int m = maze.length; 
        int n = maze[0].length;

        int[][] dis = new int[m][n];

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                dis[i][j] = Integer.MAX_VALUE;
            }
        }

        Queue<int[]> q = new LinkedList<>();

        int[][] DIRECTIONS = new int[][]{{0,1}, {1,0}, {-1,0}, {0,-1}};
        q.offer(new int[]{entrance[0], entrance[1]});
        dis[entrance[0]][entrance[1]] = 0;
        maze[entrance[0]][entrance[1]] = '+';

        while(!q.isEmpty()){
            int[] curr = q.poll();
            int R = curr[0];
            int C = curr[1];

            for(int[] dir : DIRECTIONS){
                int nR = R + dir[0];
                int nC = C + dir[1];

                if(nR<0 || nR>=m || nC<0 || nC>=n || maze[nR][nC]=='+'){
                    continue;
                }

                if(dis[R][C] + 1 < dis[nR][nC]){
                    dis[nR][nC] = dis[R][C] + 1;
                    q.offer(new int[]{nR, nC});
                }
            }
        }

        int res = Integer.MAX_VALUE;

        
        for (int i = 0; i < n; i++) {
            if (dis[0][i] != 0) {
                res = Math.min(res, dis[0][i]);  
            }
            if (dis[m-1][i] != 0) {
                res = Math.min(res, dis[m-1][i]);  
            }
        }

        
        for (int i = 0; i < m; i++) {
            if (dis[i][0] != 0) {
                res = Math.min(res, dis[i][0]);  
            }
            if (dis[i][n-1] != 0) {
                res = Math.min(res, dis[i][n-1]);  
            }
        }

        
        return res == Integer.MAX_VALUE ? -1 : res;

    }
}