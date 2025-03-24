class Solution {

    //RECURANCE
    // private int recurse(int idx, int[] nums){
    //     if(idx<0) return 0;

    //     if(idx==0) return nums[0];

    //     int pick = nums[idx] + recurse(idx-2, nums);
    //     int not = 0 + recurse(idx-1, nums);

    //     return Math.max(pick, not);
    // }

    //MEMO
    private int recurse(int idx, int[] nums, int[] dp){
        if(idx<0) return 0;

        if(idx==0) return nums[0];
        
        if(dp[idx]!=-1) return dp[idx];
        int pick = nums[idx] + recurse(idx-2, nums, dp);
        int not = 0 + recurse(idx-1, nums, dp);

        return dp[idx] = Math.max(pick, not);
    }

    public int rob(int[] nums) {
        if(nums.length==1) return nums[0];
        
        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        dp[1] = Math.max(dp[0], nums[1]);

        for(int i=2; i<nums.length; i++){
            dp[i] = Math.max(nums[i]+dp[i-2], dp[i-1]);
        }

        return dp[nums.length-1];
    }
}