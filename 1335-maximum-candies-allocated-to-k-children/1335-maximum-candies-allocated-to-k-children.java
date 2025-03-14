class Solution {
    public int maximumCandies(int[] candies, long k) {
        long total = 0;
        for (int candy : candies) {
            total += candy;
        }
    
        if (total < k) return 0;

        long max = 0;
        long low = 1, high = total/k;

        while (low <= high) {
            long mid = low + (high - low) / 2;  
            long requiredChildren = k;  
            boolean canDistribute = false;

            for (int candy : candies) {
                requiredChildren -= candy / mid;  
                if (requiredChildren <= 0) {
                    canDistribute = true;
                    break;
                }
            }

            if (canDistribute) {
                max = mid;  
                low = mid + 1;
            } else {
                high = mid - 1;  
            }
        }

        return (int) max;  
    }
}