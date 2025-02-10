class Solution {
    class Node{
        int r;
        int c;
        int dis;

        Node(int r, int c, int dis){
            this.r = r;
            this.c = c;
            this.dis = dis;
        }
    }

    public int[][] updateMatrix(int[][] mat) {
        int m = mat.length; 
        int n = mat[0].length;

        boolean[][] vis = new boolean[m][n];
        int[][] res = new int[m][n];

        Queue<Node> q = new LinkedList<>();

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(mat[i][j] == 0){
                    q.add(new Node(i, j, 0));
                    vis[i][j] = true;
                }
            }
        }

        int[][] directions = {{0,1}, {1,0}, {-1,0}, {0,-1}};

        while(!q.isEmpty()){
            Node curr = q.poll();

            for(int[] dir: directions){
                int nx = curr.r + dir[0];
                int ny = curr.c + dir[1];
                if(nx>=0 && nx<m && ny>=0 && ny<n && vis[nx][ny]==false && res[nx][ny]<=curr.dis+1){
                    vis[nx][ny] = true;
                    res[nx][ny] = curr.dis+1;
                    q.add(new Node(nx, ny, curr.dis+1));
                }   
            }

        }

        return res;
    }
}