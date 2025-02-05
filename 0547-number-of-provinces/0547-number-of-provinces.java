class Solution {
    public void dfs(ArrayList<ArrayList<Integer>> adj, boolean[] visited, int node){
        visited[node] = true;
        
        for(int i: adj.get(node)){
            if(!visited[i]){
                dfs(adj, visited, i);
            }
        }
    }

    public int findCircleNum(int[][] isConnected) {
        boolean[] visited = new boolean[isConnected.length];
        int res = 0;

        //Convert to adj list
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();

        for(int i=0; i<isConnected.length; i++){
            adj.add(new ArrayList<>());
        }

        for(int i=0; i<isConnected.length; i++){
            for(int j=0; j<isConnected.length; j++){
                if(i!=j && isConnected[i][j]==1){
                    adj.get(i).add(j);
                    adj.get(j).add(i);
                }
            }
        }

        for(int i=0; i<isConnected.length; i++){
            if(!visited[i]){
                res++;
                dfs(adj, visited, i);
            }
        }

        return res;
    }
}