import java.util.Arrays;

class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        int[] dis = new int[n];
        Arrays.fill(dis, Integer.MAX_VALUE);
        dis[k - 1] = 0;  

        for (int i = 0; i < n - 1; i++) {
            for (int[] time : times) {
                int u = time[0] - 1;  
                int v = time[1] - 1;  
                int w = time[2];   

                if (dis[u]!= Integer.MAX_VALUE && dis[u] + w < dis[v]) {
                    dis[v] = dis[u] + w;
                }
            }
        }

        
        int res = -1;
        for (int i : dis) {
            if (i == Integer.MAX_VALUE) {
                return -1;  
            }
            System.out.println(i);
            res = Math.max(res, i); 
        }

        return res;
    }
}
