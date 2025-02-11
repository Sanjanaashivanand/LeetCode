class Solution {
    private int m;
    private int n;
    private char[][] board;

    public void dfs(int r, int c){
        if(r<0 || r>=m || c<0 || c>=n || board[r][c]!='O'){
            return;
        }

        board[r][c] = 'S';

        dfs(r+1, c);
        dfs(r-1, c);
        dfs(r, c+1);
        dfs(r, c-1);

        return;
    }

    public void solve(char[][] board) {
        this.m = board.length;
        this.n = board[0].length;
        this.board = board;

        for(int i=0; i<m; i++){
            if(board[i][0]=='O') dfs(i, 0);
            if(board[i][n-1] == 'O') dfs(i, n-1);
        }

        for(int j=0; j<n; j++){
            if(board[0][j]=='O') dfs(0, j);
            if(board[m-1][j]=='O') dfs(m-1, j);
        }

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(board[i][j] == 'S'){
                    board[i][j] = 'O';
                }
                else if(board[i][j] == 'O'){
                    board[i][j] = 'X';
                }
            }
        }
        
    }
}