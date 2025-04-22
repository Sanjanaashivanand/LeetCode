class Solution {
    public int minCostClimbingStairs(int[] nums) {
        int[] dp = new int[nums.length];

        dp[0] = nums[0];
        dp[1] = nums[1];

        for(int i=2; i<nums.length;i++){
            dp[i] = nums[i] + Math.min(dp[i-1], dp[i-2]);
        }

        return Math.min(dp[dp.length-1], dp[dp.length-2]);
    }
}