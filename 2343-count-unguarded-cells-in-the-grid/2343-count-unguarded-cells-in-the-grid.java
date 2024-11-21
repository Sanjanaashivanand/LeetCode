class Solution {
    public int countUnguarded(int m, int n, int[][] guards, int[][] walls) {
        int[][] grid = new int[m][n];

        for(int[] guard: guards){
            grid[guard[0]][guard[1]] = 2;
        }

        for(int[] wall: walls){
            grid[wall[0]][wall[1]] = 2;
        }

        int[][] DIRECTIONS = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

        for(int[] guard:guards){
            for(int[] dir: DIRECTIONS){
                int x = guard[0];
                int y = guard[1];
                int dx = dir[0];
                int dy = dir[1];

                while(x + dx >= 0 && x + dx < m &&
                        y + dy >= 0 && y + dy < n &&
                        grid[x + dx][y + dy] < 2){
                            x += dx;
                            y += dy;
                            grid[x][y] = 1;
                        }
            }
        }

        int unguarded = 0;

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(grid[i][j] == 0){
                    unguarded++;
                }
            }
        }

        return unguarded;
    }
}