class Solution {
    private List<Integer> res;
    private int[][] adj;

    public boolean dfs(int node, boolean[] vis, boolean[] pathVisited, boolean[] check){
        vis[node] = true;
        pathVisited[node] = true;

        for(int i: adj[node]){
            if(!vis[i]){
                if(dfs(i, vis, pathVisited, check)){
                    return true;
                }
            }
            else if(pathVisited[i]){
                return true;
            }
        }

        pathVisited[node]=false;
        check[node] = true;
        return false;
    }

    public List<Integer> eventualSafeNodes(int[][] graph) {
        res = new ArrayList<>();
        this.adj = graph;
        boolean[] vis = new boolean[graph.length];
        boolean[] pathVis = new boolean[graph.length];
        boolean[] check = new boolean[graph.length];

        for(int i=0; i<graph.length; i++){
            if(!vis[i]){
                dfs(i, vis, pathVis, check);
            }
        }

        for(int i=0; i<graph.length; i++){
            if(check[i]){
                res.add(i);
            }
        }

        return res;
    }
}