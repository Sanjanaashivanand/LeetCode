class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] len = new int[nums.length];
        Arrays.fill(len,1);

        for(int i=0; i<nums.length; i++){
            for(int j=0; j<i; j++){
                if(nums[j]<nums[i]){
                    len[i] = Math.max(len[i], len[j]+1);
                }
            }
        }

        int res = -1;
        for(int i:len){
            res = Math.max(res,i);
        }

        return res;
    }
}