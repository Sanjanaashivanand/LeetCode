class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        List<Integer> row = new ArrayList<>();
        List<Integer> col = new ArrayList<>();

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(matrix[i][j] == 0){
                    row.add(i);
                    col.add(j);
                }
            }
        }

        for(int i: row){
            for(int j=0; j<n; j++){
                matrix[i][j] = 0;
            }
        }

        for(int i=0; i<m; i++){
            for(int j:col){
                matrix[i][j] = 0;
            }
        }
    }
}