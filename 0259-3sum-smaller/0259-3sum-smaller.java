import java.util.Arrays;

class Solution {
    public int threeSumSmaller(int[] nums, int target) {
        int res = 0;
        int n = nums.length;

        Arrays.sort(nums);

        for (int i = 0; i < n - 2; i++) {
            int left = i + 1;
            int right = n - 1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum < target) {
                    res += (right - left);
                    left++;  
                } else {
                    right--;  
                }
            }
        }

        return res;
    }
}
