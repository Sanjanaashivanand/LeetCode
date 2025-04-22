class Solution {
    int n;
    List<Integer> res;

    public boolean dfs(int node, int[][] graph, boolean[] vis, boolean[] pathVis, boolean[] notCycle){
        vis[node] = true;
        pathVis[node] = true;

        for(int i : graph[node]){
            if(!vis[i]){
                if(dfs(i, graph, vis, pathVis, notCycle)){
                    return true;
                }
            }
            else if(pathVis[i]){
                return true;
            }
        }

        pathVis[node] = false;
        notCycle[node] = true;
        return false;
    }


    public List<Integer> eventualSafeNodes(int[][] graph) {
        res = new ArrayList<>();
        this.n = graph.length;

        boolean[] vis = new boolean[n];
        boolean[] notCycle = new boolean[n];
        boolean[] pathVis = new boolean[n];

        for(int i=0; i<n; i++){
            if(!vis[i]){
                dfs(i, graph, vis, pathVis, notCycle);
            }
        }

        for(int i=0; i<n; i++){
            if(notCycle[i]){
                res.add(i);
            }
        }

        return res;

    }
}