class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        int i = 0, j = 0;
        long res = 0, sum = 0;
        HashMap<Integer, Integer> window = new HashMap<>();

        while (j < nums.length) {
            // Add nums[j] to the window and update the sum
            window.put(nums[j], window.getOrDefault(nums[j], 0) + 1);
            sum += nums[j];

            // If the window size exceeds k, remove nums[i]
            if (j - i + 1 > k) {
                sum -= nums[i];
                window.put(nums[i], window.get(nums[i]) - 1);
                if (window.get(nums[i]) == 0) {
                    window.remove(nums[i]);
                }
                i++;
            }

            // Check if the window is valid (size == k and all unique)
            if (j - i + 1 == k && window.size() == k) {
                res = Math.max(res, sum);
            }

            j++;
        }

        return res;
    }
}