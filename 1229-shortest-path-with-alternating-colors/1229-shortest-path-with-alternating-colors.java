class Solution {
    public int[] shortestAlternatingPaths(int n, int[][] redEdges, int[][] blueEdges) {
        List<List<int[]>> adj = new ArrayList<>();
        for(int i=0; i<n; i++) adj.add(new ArrayList<>());

        for(int[] edge : redEdges){
            adj.get(edge[0]).add(new int[]{edge[1], 0});
        }

        for(int[] edge : blueEdges){
            adj.get(edge[0]).add(new int[]{edge[1], 1});
        }

        int[] res = new int[n];
        Arrays.fill(res, -1);
        boolean[][] visit = new boolean[n][2];
        Queue<int[]> q = new LinkedList<>();

        q.offer(new int[] { 0, 0, -1 });
        res[0] = 0;
        visit[0][0] = visit[0][1] = true;
        
        while(!q.isEmpty()){
            int[] curr = q.poll();
            int node = curr[0];
            int dis = curr[1];
            int prevColor = curr[2];

            for(int[] next : adj.get(node)){
                int neigh = next[0];
                int color = next[1];

                if(!visit[neigh][color] && color!=prevColor){
                    if(res[neigh] == -1){
                        res[neigh] = 1 + dis;
                    }

                    visit[neigh][color] = true;
                    q.offer(new int[]{neigh, 1+dis, color});
                }
            }

        }

        return res;
    }
}