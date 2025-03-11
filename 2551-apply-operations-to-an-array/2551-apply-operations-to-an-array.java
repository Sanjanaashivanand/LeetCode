class Solution {
    public int[] applyOperations(int[] nums) {
        for(int i=0; i<nums.length-1; i++){
            if(nums[i] == nums[i+1]){
                nums[i] = 2 * nums[i];
                nums[i+1] = 0;
            }
        }

        int[] res = new int[nums.length];
        int k = 0;
        for(int i=0; i<nums.length; i++){
            if(nums[i]!=0){
                res[k++] = nums[i];
            }
        }

        return res;
    }
}