class Solution {
    public int[][] generateMatrix(int n) {
        int top = 0;
        int bottom = n-1;
        int left = 0;
        int right = n-1;
        int[][] res = new int[n][n];

        int curr = 1;

        while(left<=right && top<=bottom){
            //Move left to right
            for(int i=left; i<=right; i++){
                res[top][i] = curr++;
            }
            top++;

            //Move top to bottom
            for(int i=top; i<=bottom; i++){
                res[i][right] = curr++;
            }
            right--;

            //Move right to left
            for(int i=right; i>=left; i--){
                res[bottom][i] = curr++;
            }
            bottom--;

            //Move bottom to top
            for(int i=bottom; i>=top; i--){
                res[i][left] = curr++;
            }
            left++;
        }

        return res;
    }
}