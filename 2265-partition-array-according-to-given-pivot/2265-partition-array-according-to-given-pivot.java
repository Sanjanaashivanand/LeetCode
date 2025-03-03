class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        int n = nums.length;
        int[] copy = new int[n];
        int count = 0;

        int k = 0;
        for(int i=0; i<n; i++){
            if(nums[i] < pivot){
                copy[k++] = nums[i];
            }
            else if(nums[i] == pivot){
                count++;
            }
        }

        for(int i=0; i<count; i++){
            copy[k++] = pivot;
        }

        for(int i=0; i<n; i++){
            if(nums[i] > pivot){
                copy[k++] = nums[i];
            }
        }

        return copy;

    }
}