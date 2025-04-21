class Solution {
    public int numberOfArrays(int[] differences, int lower, int upper) {
        long sum = 0;
        long minSum = 0;
        long maxSum = 0;

        for (int diff : differences) {
            sum += diff;
            minSum = Math.min(minSum, sum);
            maxSum = Math.max(maxSum, sum);
        }

        long xLow = lower - minSum;   
        long xHigh = upper - maxSum;  

        if (xLow > xHigh) {
            return 0; // No valid 'x' values if the range is inverted
        }

        return (int) (xHigh - xLow + 1);
    }
}
