class Solution {
    private boolean[][] visited;
    private String word;
    private char[][] board;

    private boolean check(int i, int j, int idx){
        if(idx == word.length()){
            return true;
        }

        if(i<0 || i>=board.length || 
            j<0 || j>=board[0].length ||
            board[i][j] != word.charAt(idx) || visited[i][j]){
                return false;
            }
        
        visited[i][j] = true;
        if(check(i-1, j, idx+1) ||
            check(i+1, j, idx+1) ||
            check(i, j-1, idx+1) ||
            check(i, j+1, idx+1)){
                return true;
            }

        visited[i][j] = false;
        return false;
    }

    public boolean exist(char[][] board, String word) {
        this.board = board;
        this.word = word;
        visited = new boolean[board.length][board[0].length];

        for(int i=0;i<board.length; i++){
            for(int j=0;j<board[0].length;j++){
                if(board[i][j] == word.charAt(0) && check(i, j, 0)){
                    return true;
                }
            }
        }
        return false;
    }
}