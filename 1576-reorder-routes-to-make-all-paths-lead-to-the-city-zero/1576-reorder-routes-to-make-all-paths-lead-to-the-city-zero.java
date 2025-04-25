class Solution {
    public int minReorder(int n, int[][] connections) {
        HashSet<String> set = new HashSet<>();

        List<List<Integer>> adj = new ArrayList<>();
        for(int i=0; i<n; i++) adj.add(new ArrayList<>());

        for(int[] edge : connections){
            set.add(edge[0] + " to " + edge[1]);

            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }

        int changes = 0;
        Queue<Integer> q = new LinkedList<>();
        boolean[] vis = new boolean[n];

        q.add(0);
        vis[0]=true;

        while(!q.isEmpty()){
            int curr = q.poll();

            for(int neigh : adj.get(curr)){
                if(!vis[neigh]){
                    if(set.contains(curr + " to " + neigh)){
                        changes++;
                    }
                    q.add(neigh);
                    vis[neigh] = true;
                }
            }
        }


        return changes;
    }
}