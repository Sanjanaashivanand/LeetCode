class Solution {
    public int orangesRotting(int[][] grid) {
        Queue<Pair> queue = new LinkedList<>();
        int fresh = 0;
        int time = 0;

        int m = grid.length;
        int n = grid[0].length;

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(grid[i][j]==2){
                    queue.add(new Pair<>(i,j));
                }
                else if(grid[i][j]==1){
                    fresh++;
                }
            }
        }

        int[][] directions = {{1,0}, {-1,0}, {0,-1}, {0,1}};

        while(!queue.isEmpty() && fresh>0){
            int len = queue.size();

            for(int i=0; i<len; i++){
                Pair<Integer, Integer> cord = queue.poll();
                int x = cord.getKey();
                int y = cord.getValue();

                for(int[] dir: directions){
                    int xn = x + dir[0];
                    int yn = y + dir[1];

                    if(xn<0 || xn>=m || 
                        yn<0 || yn>=n){
                            continue;
                        }

                    if(grid[xn][yn]==1){
                        fresh--;
                        grid[xn][yn]=2;
                        queue.add(new Pair<>(xn, yn));
                    }
                }
            }
            time++;

        }

        if(fresh==0){
            return time;
        }
        return -1;

    }
}