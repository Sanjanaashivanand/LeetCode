class Solution {
    public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        List<List<Integer>> adj = new ArrayList<>();
        for(int i=0; i<n; i++){
            adj.add(new ArrayList<>());
        }

        for(int i=0; i<manager.length; i++){
            if(manager[i]==-1) continue;
            adj.get(manager[i]).add(i);
        }

        boolean[] vis = new boolean[n];
        int[] dis = new int[n];
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{headID, 0});
        dis[headID] = informTime[headID];

        while(!q.isEmpty()){
            int[] curr = q.poll();
            int node = curr[0];
            int time = curr[1];

            for(int neigh : adj.get(node)){
                if(!vis[neigh]){
                    dis[neigh] = time + informTime[node];
                }

                vis[neigh] = true;
                q.offer(new int[]{neigh, time + informTime[node]});
            }
        }

        int res = -1;
        for(int i: dis){
            res = Math.max(res, i);
        }

        return res;
    }
}