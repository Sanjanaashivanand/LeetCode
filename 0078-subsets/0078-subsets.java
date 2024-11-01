class Solution {
    private List<List<Integer>> res = new ArrayList<>();
    private int[] nums;

    private void generateSubarray(List<Integer> path, int idx){
        if(idx == nums.length){
            res.add(path);
            return;
        }

        List<Integer> copy = new ArrayList<>(path);
        copy.add(nums[idx]);
        generateSubarray(copy, idx+1);
        generateSubarray(path, idx+1);
    }

    public List<List<Integer>> subsets(int[] nums) {
        this.nums = nums;
        List<Integer> path = new ArrayList<>();
        generateSubarray(path, 0);
        return res;
    }
}