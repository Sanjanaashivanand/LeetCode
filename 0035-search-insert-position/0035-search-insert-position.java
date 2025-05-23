class Solution {
    public int searchInsert(int[] nums, int target) {
        int high = nums.length-1;
        int low = 0;
        int mid = -1;

        if(target<nums[0]) return 0;
        if(target>nums[nums.length-1]) return nums.length;

        while(low<=high){
            mid = (low+high)/2;

            if(nums[mid]==target){
                return mid;
            }

            if(target > nums[mid]){
                low = mid+1;
            }
            else{
                high = mid-1;
            }
        }

        return low;
    }
}