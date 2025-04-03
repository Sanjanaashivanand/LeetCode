class Solution {
    class Pair{
        int idx;
        int height;

        Pair(int idx, int height){
            this.idx = idx;
            this.height = height;
        }
    }

    public int maxHistogram(int[][] dp, int row){
        Stack<Pair> stack = new Stack<>();
        int max = 0;

        for(int i=0; i<dp[0].length; i++){
            int startIdx = i;
            int currHeight = dp[row][i];

            while(!stack.isEmpty() && stack.peek().height > currHeight){
                Pair top = stack.pop();
                max = Math.max(max, top.height *  (i - top.idx));
                startIdx = top.idx;
            }

            stack.push(new Pair(startIdx, currHeight));
        }

        while(!stack.isEmpty()){
            Pair top = stack.pop();
            max = Math.max(max, top.height *  (dp[0].length - top.idx));
        }

        return max;
    }

    public int maximalRectangle(char[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] dp = new int[m][n];
        int max = 0;

        for(int i=0; i<n; i++){
            if(matrix[0][i] == '1'){
                dp[0][i] = 1;
            }
        }

        max = Math.max(max, maxHistogram(dp, 0));

        for(int i=1; i<m; i++){
            for(int j=0; j<n; j++){
                if(matrix[i][j] == '1'){
                    dp[i][j] = dp[i-1][j] + 1;
                }
            }

            max = Math.max(max, maxHistogram(dp, i));
        }

        return max;
    }
}