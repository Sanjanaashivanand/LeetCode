class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n1 = nums1.length;
        int n2 = nums2.length;

        // Handle edge case where one array is empty
        if (n1 == 0) {
            return findMedianOfSingleArray(nums2);
        }
        if (n2 == 0) {
            return findMedianOfSingleArray(nums1);
        }

        // Ensure nums1 is the smaller array to reduce the binary search space
        if (n1 > n2) {
            return findMedianSortedArrays(nums2, nums1);
        }

        // Total number of elements to the left of the median
        int n_half = (n1 + n2 + 1) / 2;

        int low = 0;
        int high = n1;

        while (low <= high) {
            int mid1 = (low + high) / 2;
            int mid2 = n_half - mid1;

            // Edge cases where the index may go out of bounds for nums1 or nums2
            int l1 = (mid1 == 0) ? Integer.MIN_VALUE : nums1[mid1 - 1];
            int l2 = (mid2 == 0) ? Integer.MIN_VALUE : nums2[mid2 - 1];

            int r1 = (mid1 == n1) ? Integer.MAX_VALUE : nums1[mid1];
            int r2 = (mid2 == n2) ? Integer.MAX_VALUE : nums2[mid2];

            // Check if the partition is correct
            if (l1 <= r2 && l2 <= r1) {
                if ((n1 + n2) % 2 == 0) {
                    return (double) (Math.max(l1, l2) + Math.min(r1, r2)) / 2.0;
                } else {
                    return Math.max(l1, l2);
                }
            } else if (l1 > r2) {
                high = mid1 - 1;
            } else {
                low = mid1 + 1;
            }
        }

        return 0;
    }

    // Helper function to calculate the median of a single array
    private double findMedianOfSingleArray(int[] nums) {
        int n = nums.length;
        if (n % 2 == 0) {
            return (nums[n / 2 - 1] + nums[n / 2]) / 2.0;
        } else {
            return nums[n / 2];
        }
    }
}
