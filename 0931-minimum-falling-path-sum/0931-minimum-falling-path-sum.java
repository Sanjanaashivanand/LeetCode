class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int n = matrix.length;
        int[][] copy = new int[n][n];


        for(int i=0; i<n; i++){
            copy[0][i] =matrix[0][i];
        }

        for(int i=1; i<n; i++){
            for(int j=0; j<n; j++){
                copy[i][j] = Integer.MAX_VALUE;
                if(j!=0){
                    copy[i][j] = Math.min(matrix[i][j] + copy[i-1][j-1], copy[i][j]);
                }
                if(j!=n-1){
                    copy[i][j] = Math.min(matrix[i][j] + copy[i-1][j+1], copy[i][j]);
                }
                copy[i][j] = Math.min(matrix[i][j] + copy[i-1][j], copy[i][j]);

            }
            
        }

        int res = copy[n-1][0];
        for(int i=1; i<n; i++){
            if(copy[copy.length-1][i]<res){
                res = copy[copy.length-1][i];
            }
        }
       
       return res;

       


        
    }
}