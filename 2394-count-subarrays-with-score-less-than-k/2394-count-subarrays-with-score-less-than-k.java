class Solution {
    public long countSubarrays(int[] nums, long k) {
        long res = 0;
        long sum = 0;
        int n = nums.length;

        int i = 0;

        for(int j=0; j<n; j++){
            sum += nums[j];

            while(sum * (j-i+1) >= k){
                sum -= nums[i];
                i++;
            }

            res += j-i+1;
        }



        return res;
    }
}