class Solution {
    public int permute(int idx, int[] nums, int target){
        if(idx == nums.length && (target == 0)){
            return 1;
        }
        if(idx>=nums.length) return 0;

        int add = permute(idx+1, nums, target+nums[idx]);
        int sub = permute(idx+1, nums, target-nums[idx]);

        return add+sub;
    }

    public int findTargetSumWays(int[] nums, int target) {
        return permute(0, nums, target);
    }
}