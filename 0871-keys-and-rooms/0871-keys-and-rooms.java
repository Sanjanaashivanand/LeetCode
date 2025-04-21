class Solution {
    int n;

    public void dfs(int node, List<List<Integer>> rooms, boolean[] vis){
        vis[node] = true;

        for(int next : rooms.get(node)){
            if(!vis[next]){
                dfs(next, rooms, vis);
            }
        }
    }

    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        this.n = rooms.size();
        boolean[] vis = new boolean[n];
        vis[0] = true;

        for(int next : rooms.get(0)){
            dfs(next, rooms, vis);
        }

        for(int i=0; i<n; i++){
            if(!vis[i]){
                return false;
            }
        }

        return true;
    }
}