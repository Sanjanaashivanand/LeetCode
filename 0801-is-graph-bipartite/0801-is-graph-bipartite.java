import java.util.*;

class Solution {
    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        int[] set = new int[n];  
        Arrays.fill(set, -1);    

        boolean[] vis = new boolean[n]; 
        Queue<Integer> q = new LinkedList<>();
        
        
        for (int i = 0; i < n; i++) {
            if (set[i] == -1) {  
                q.add(i);
                set[i] = 0;  

                while (!q.isEmpty()) {
                    int curr = q.poll();
                    
                    for (int neighbor : graph[curr]) {
                        if (set[neighbor] == -1) {    
                            set[neighbor] = 1 - set[curr];
                            q.add(neighbor);
                        } else if (set[neighbor] == set[curr]) { 
                            return false;
                        }
                    }
                }
            }
        }

        return true; // If no conflict was found
    }
}
