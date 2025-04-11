class Solution {
    public int countNegatives(int[][] grid) {
        int count = 0;
        int m = grid.length;
        int n = grid[0].length;

        for(int[] row : grid){
            int low = 0;
            int high = n-1;

            while(low<=high){
                int mid=(low+high)/2;

                if (row[mid] < 0) {
                    high = mid - 1;
                } else {
                    low = mid + 1;  
                }
            }

            count += (n-low);
        }

        return count;
    }
}