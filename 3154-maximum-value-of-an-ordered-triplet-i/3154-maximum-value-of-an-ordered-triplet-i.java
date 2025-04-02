class Solution {
    public long maximumTripletValue(int[] nums) {
        long res = 0;
        
        int n = nums.length;
        int[] leftMax = new int[n];
        int[] rightMax = new int[n];

        for(int i=1; i<n; i++){
            leftMax[i] = Math.max(leftMax[i-1], nums[i-1]);
            rightMax[n-i-1] = Math.max(rightMax[n-i], nums[n-i]);
        }

        for(int j=1; j<n-1; j++){
            res = Math.max(res, (long)(leftMax[j] - nums[j]) * rightMax[j]);
        }

        return res;

    }
}