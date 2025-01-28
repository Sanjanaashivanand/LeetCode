class Solution {
    public boolean canPartition(int[] nums) {
        int sum = 0;
        for(int i: nums) sum+=i;

        if(sum%2!=0) return false;

        HashSet<Integer> dp = new HashSet<>();
        dp.add(nums[0]);

        for(int i=1; i<nums.length; i++){
            HashSet<Integer> newDP = new HashSet<>();
            for(Integer j : dp){
                int newSum = nums[i] + j;
                if(newSum == sum/2) return true;
                newDP.add(newSum);
                newDP.add(j);
            }
            dp = newDP;
        }

        return dp.contains(sum/2);
    }
}