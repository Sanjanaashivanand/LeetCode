class Solution {
    public int uniquePaths(int m, int n) {
        int[] lastRow = new int[n];
        Arrays.fill(lastRow, 1);

        for(int i=m-1; i>=1; i--){
            int[] newRow = new int[n];
            Arrays.fill(newRow, 1);

            for(int j=n-2; j>=0; j--){
                newRow[j] = lastRow[j] + newRow[j+1];
            }

            lastRow = newRow;
        }

        return lastRow[0];

    }
}