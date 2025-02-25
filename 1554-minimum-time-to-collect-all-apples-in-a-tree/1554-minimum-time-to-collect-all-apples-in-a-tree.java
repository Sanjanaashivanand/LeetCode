class Solution {
    public int dfs(int node, List<List<Integer>> adj, boolean[] vis, List<Boolean> hasApple) {
        vis[node] = true;
        int totalTime = 0;

        
        for (int neigh : adj.get(node)) {
            if (!vis[neigh]) {
                int time = dfs(neigh, adj, vis, hasApple);

                if (time > 0 || hasApple.get(neigh)) {
                    totalTime += time + 2; 
                }
            }
        }

        return totalTime;
    }

    public int minTime(int n, int[][] edges, List<Boolean> hasApple) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }


        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }

        boolean[] vis = new boolean[n];

        // Start DFS from the root (node 0)
        return dfs(0, adj, vis, hasApple);
    }
}
