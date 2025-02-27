class Solution {
    class Node{
        int distance,row,col;
        Node(int distance,int row,int col){
            this.distance=distance;
            this.row=row;
            this.col=col;
        } 
    }

    public int swimInWater(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        Queue<Node> q = new PriorityQueue<>((x,y)->x.distance-y.distance);

        int[][]dist = new int[m][n];
        for(int []row:dist){
            Arrays.fill(row,Integer.MAX_VALUE);
        }

        dist[0][0]=grid[0][0];
        q.add(new Node(grid[0][0],0,0));

        int[][] DIRECTIONS = {{0,1}, {1,0}, {-1,0}, {0,-1}};

        while(!q.isEmpty()){
            Node curr = q.poll();
            int diff = curr.distance;
            int r = curr.row;
            int c = curr.col;

            if(r==m-1 && c==n-1) return diff;

            for(int[] dir : DIRECTIONS){
                int nR = r + dir[0];
                int nC = c + dir[1];

                if(nR<0 || nR>=m || nC<0 || nC>=n) continue;

                int newEffort = Math.max(grid[nR][nC], diff);

                if(newEffort<dist[nR][nC]){
                    dist[nR][nC] = newEffort;
                    q.offer(new Node(newEffort, nR, nC));
                }
            }
        }

        return 0;


    }
}