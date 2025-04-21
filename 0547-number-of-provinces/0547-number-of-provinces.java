class Solution {
    int n;

    public void dfs(int i, List<List<Integer>> adj, boolean[] vis){
        vis[i] = true;

        for(int neigh : adj.get(i)){
            if(!vis[neigh]){
                dfs(neigh, adj, vis);
            }
        }
    }

    public int findCircleNum(int[][] isConnected) {
        this.n = isConnected.length;
        List<List<Integer>> adj = new ArrayList<>();

        for(int i=0; i<n; i++){
            adj.add(new ArrayList<>());
        }

        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(isConnected[i][j]==1){
                    adj.get(i).add(j);
                    adj.get(j).add(i);
                }
            }
        }

        boolean[] visited = new boolean[n];
        int res = 0;

        for(int i=0; i<n; i++){
            if(!visited[i]){
                res++;
                dfs(i, adj, visited);
            }
        }

        return res;
    }
}