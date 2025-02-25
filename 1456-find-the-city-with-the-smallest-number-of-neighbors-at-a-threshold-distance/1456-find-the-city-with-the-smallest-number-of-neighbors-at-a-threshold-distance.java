class Solution {
    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        int[][] adj = new int[n][n];
        for(int i=0;i<n;i++){
            for(int j=0; j<n; j++){
                if(i==j){
                    adj[i][j] = 0;
                }
                else{
                    adj[i][j]=Integer.MAX_VALUE;
                }
            }
        }

        for(int[] edge: edges){
            adj[edge[0]][edge[1]] = edge[2];
            adj[edge[1]][edge[0]] = edge[2];
        }

        for(int k=0; k<n; k++){
            for(int i=0; i<n; i++){
                for(int j=0; j<n; j++){
                    if(adj[i][k]!=Integer.MAX_VALUE && adj[k][j]!=Integer.MAX_VALUE){
                        adj[i][j] = Math.min(adj[i][j], adj[i][k]+adj[k][j]);
                    }
                }
            }
        }

        int min = n;
        int res = 0;
        for(int i=0; i<n; i++){
            int count = 0;
            for(int j=0; j<n; j++){
                if(adj[i][j] <= distanceThreshold && i!=j){
                    count++;
                }
            }

            if(count<=min){
                min = count;
                res = i;
            }
        }

        return res;
    }
}