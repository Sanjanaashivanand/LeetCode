class Solution {
    public int waysToSplitArray(int[] nums) {
        if(nums.length==2){
            if(nums[0]>=nums[1]){
                return 1;
            }
            else{
                return 0;
            }
        }
        long[] l = new long[nums.length];
        long[] r = new long[nums.length];

        l[0] = nums[0];
        r[nums.length-1]=nums[nums.length-1];

        for(int i=1; i<nums.length; i++){
            l[i] = l[i-1]+nums[i];
            r[nums.length-1-i] = r[nums.length-i]+nums[nums.length-1-i];
        }
       
        int res = 0;
        for(int i=0; i<nums.length-1;i++){
            if(l[i]>=r[i+1]){
                res++;
            }
        }

        return res;
    }
}