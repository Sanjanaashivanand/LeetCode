class Solution {
    public void reverse(int[] nums, int start, int end){
        int n = (start + end);
        for(int i=start; i<n/2; i++){
            int temp = nums[i];
            nums[i] = nums[n - i - 1];
            nums[n - i - 1] = temp; 
        }
        return;
    }

    public void nextPermutation(int[] nums) {
        //1. Find the break point 
        int n = nums.length;
        int breakPoint = -1;

        for(int i=n-2; i>=0; i--){
            if(nums[i] < nums[i+1]){
                breakPoint = i;
                break;
            }
        }
        

        if(breakPoint == -1){
            reverse(nums, 0, n);
            return;
        }

        //Swap the element at break point with the next largest element in th right
        int next = 0;
        for(int i=n-1; i>breakPoint; i--){
            System.out.println(nums[i]);
            if(nums[i] > nums[breakPoint]){
                next = i; 
                break;
            }
        }

        int temp = nums[breakPoint];
        nums[breakPoint] = nums[next];
        nums[next] = temp;

        reverse(nums, breakPoint+1, n);

        return;
    }
}