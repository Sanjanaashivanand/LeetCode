class Solution {

    //RECURANCE
    private int recurse(int idx, int[] nums, int[] dp){
        if(idx<0) return 0;

        if(idx==0) return nums[0];

        if(dp[idx]!=-1) return dp[idx];

        int pick = nums[idx] + recurse(idx-2, nums, dp);
        int not = 0 + recurse(idx-1, nums, dp);
        
        return dp[idx] = Math.max(pick, not);
    }

    // private int recurse(int idx, int[] nums, int[] dp){
    //     if(idx<0) return 0;

    //     if(idx==0) return nums[0];
        
    //     if(dp[idx]!=-1) return dp[idx];
    //     int pick = nums[idx] + recurse(idx-2, nums, dp);
    //     int not = 0 + recurse(idx-1, nums, dp);

    //     return dp[idx] = Math.max(pick, not);
    // }

    public int rob(int[] nums) {
        int[] dp = new int[nums.length];
        Arrays.fill(dp, -1);
        return recurse(nums.length-1, nums, dp);
    }
}