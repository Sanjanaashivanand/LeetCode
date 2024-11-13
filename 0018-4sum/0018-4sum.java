class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        Set<List<Integer>> res = new HashSet<>();

        for(int i=0; i<nums.length-3; i++){
            for(int j=i+1; j<nums.length-2; j++){
                int l=j+1;
                int r = nums.length-1;

                while(l<r){
                    long sum = (long)nums[i] + nums[j] + nums[l] + nums[r];
                    if(sum == target){
                        res.add(Arrays.asList(nums[i], nums[j], nums[l], nums[r]));
                        l++;
                        r--;
                    }
                    else if(sum < target){
                        l++;
                    }
                    else{
                        r--;
                    }
                }
            }
        }

        return new ArrayList<>(res);
    }
}