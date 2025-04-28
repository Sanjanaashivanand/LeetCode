class Solution {
    private List<List<Integer>> bridges;
    private List<List<Integer>> adj;

    public void dfs(int node, int parent, boolean[] vis, int[] toi, int[] low, int time){
        vis[node] = true;
        toi[node] = time;
        low[node] = time;
        time++;

        for(int neigh : adj.get(node)){
            if(neigh==parent) continue;

            if(!vis[neigh]){
                dfs(neigh, node, vis, toi, low, time);
                low[node] = Math.min(low[neigh], low[node]);
                if(low[neigh]>toi[node]){
                    bridges.add(Arrays.asList(neigh, node));
                }
            }
            else{
                low[node] = Math.min(low[neigh], low[node]);
            }
        }
    }

    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        this.bridges = new ArrayList<>();
        this.adj = new ArrayList<>();

        for(int i=0; i<n; i++) adj.add(new ArrayList<>());

        for(List<Integer> edge : connections){
            adj.get(edge.get(0)).add(edge.get(1));
            adj.get(edge.get(1)).add(edge.get(0));
        }

        int[] toi = new int[n];
        int[] low = new int[n];
        boolean[] vis = new boolean[n];

        dfs(0, -1, vis, toi, low, 1);

        return bridges;
    }
}