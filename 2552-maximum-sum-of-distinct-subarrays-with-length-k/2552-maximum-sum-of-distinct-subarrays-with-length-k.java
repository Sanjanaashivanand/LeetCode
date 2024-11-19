class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        int i=0; 
        int j=0;

        long res = 0, currentSum=0;

        Map<Integer, Integer> window = new HashMap<>();

        while(j<nums.length){
            window.put(nums[j], window.getOrDefault(nums[j], 0) + 1);
            currentSum += nums[j];

            while (j - i + 1 > k) {
                window.put(nums[i], window.get(nums[i]) - 1);
                if (window.get(nums[i]) == 0) {
                    window.remove(nums[i]);
                }
                currentSum -= nums[i];
                i++;
            }


            // Check if the current window is valid and update the result
            if (j - i + 1 == k && window.size() == k) {
                res = Math.max(res, currentSum);
            }

            j++;
        }

        return res;
    }
}