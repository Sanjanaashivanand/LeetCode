import java.util.*;

class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        if (grid.length == 0 || grid[0][0] == 1 || grid[grid.length - 1][grid[0].length - 1] == 1) {
            return -1;  // No path if start or end is blocked
        }

        int n = grid.length;
        int[][] dis = new int[n][n];
        
    
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                dis[i][j] = Integer.MAX_VALUE;
            }
        }

    

        int[][] DIRECTIONS = {{0,1}, {1,0}, {-1,0}, {0,-1}, {1,1}, {-1,-1}, {-1,1}, {1,-1}};
        
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0, 0});  
        dis[0][0] = 1;  

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int currR = curr[0];
            int currC = curr[1];

            for (int[] dir : DIRECTIONS) {
                int nR = currR + dir[0];
                int nC = currC + dir[1];

                if (nR < 0 || nR >= n || nC < 0 || nC >= n || grid[nR][nC] == 1) {
                    continue;
                }

                
                if (dis[nR][nC] == Integer.MAX_VALUE) {
                    dis[nR][nC] = dis[currR][currC] + 1;
                    queue.offer(new int[]{nR, nC});
                }
            }
        }

        if (dis[n - 1][n - 1] == Integer.MAX_VALUE) {
            return -1;
        }
        
        return dis[n - 1][n - 1];
    }
}
