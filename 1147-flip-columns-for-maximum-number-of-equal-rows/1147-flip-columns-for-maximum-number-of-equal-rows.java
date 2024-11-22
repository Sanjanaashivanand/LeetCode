class Solution {
    public int maxEqualRowsAfterFlips(int[][] matrix) {
        HashMap<String, Integer> map = new HashMap<>();

        for(int i=0; i<matrix.length; i++){
            StringBuilder sb = new StringBuilder();

            if(matrix[i][0]==1){
                //Flip it
                for(int j=0; j<matrix[i].length; j++){
                    matrix[i][j] = matrix[i][j]==1 ? 0 : 1;
                }
            }

            for(int k : matrix[i]){
                sb.append(k);
            }

            map.put(sb.toString(), map.getOrDefault(sb.toString(), 0) + 1);
        }

        int res = 0;

        for(String s : map.keySet()){
            // System.out.println(s + " " + map.get(s));
            res = Math.max(res, map.get(s));
        }

        return res;
    }
}