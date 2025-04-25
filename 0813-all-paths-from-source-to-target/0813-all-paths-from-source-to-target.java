class Solution {
    int n;
    List<List<Integer>> res;

    public void dfs(int node, boolean[] vis, int[][] graph, ArrayList<Integer> path){
        if(node==n-1){
            res.add(new ArrayList<Integer>(path));
            return;
        }

        vis[node] = true;

        for(int neigh : graph[node]){
            if(!vis[neigh]){
                path.add(neigh);
                dfs(neigh, vis, graph, path); 
                path.removeLast();
            }
        }

        if(node!=0) vis[node] = false;
    } 

    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        this.n = graph.length;
        this.res = new ArrayList<>();
        ArrayList<Integer> path = new ArrayList<>();

        boolean[] vis = new boolean[n];
        path.add(0);

        dfs(0, vis, graph, path);

        return res;
    }
}