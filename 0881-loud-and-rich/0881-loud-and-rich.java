class Solution {
    List<List<Integer>> adj;
    int[] ans;
    int[] quiet;

    public int dfs(int node){
        if(ans[node] == -1){
            ans[node] = node;
            for(int i : adj.get(node)){
                int cand = dfs(i);
                if(quiet[cand] < quiet[ans[node]]){
                    ans[node] = cand;
                }
            }
        }
        return ans[node];
    }

    public int[] loudAndRich(int[][] richer, int[] quiet) {
        int n = quiet.length;
        ans = new int[n];
        this.quiet = quiet;
        adj = new ArrayList<>();

        for(int i=0; i<n; i++){
            adj.add(new ArrayList<>());
        }

        for(int[] con : richer){
            adj.get(con[1]).add(con[0]);
        }

        Arrays.fill(ans, -1);

        for(int i=0; i<n; i++){
            dfs(i);
        }

        return ans;
    }
}