class Solution {
    public int maximumCandies(int[] candies, long k) {
        // Calculate the total number of candies
        long total = 0;
        for (int candy : candies) {
            total += candy;
        }
        
        // If total candies are less than the required k children, return 0
        if (total < k) return 0;

        long max = 0;
        long low = 1, high = total;

        // Binary search on the number of candies each child can get
        while (low <= high) {
            long mid = low + (high - low) / 2;  // Get the middle value of candies each child can get
            long requiredChildren = k;  // Number of children we need to provide candies to
            boolean canDistribute = false;

            // Step 2: Check if it's possible to distribute `mid` candies to `k` children
            for (int candy : candies) {
                requiredChildren -= candy / mid;  // Calculate how many children can get `mid` candies from this pile
                if (requiredChildren <= 0) {
                    canDistribute = true;
                    break;
                }
            }

            // Step 3: Update binary search bounds
            if (canDistribute) {
                max = mid;  // If we can distribute, update max and try a larger value
                low = mid + 1;
            } else {
                high = mid - 1;  // If we can't distribute, try a smaller value
            }
        }

        return (int) max;  // Convert long to int for the final result
    }
}
