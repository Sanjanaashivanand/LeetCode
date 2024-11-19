class Solution {
    private List<List<Integer>> res = new ArrayList<>();
    private int[] nums;

    private void generateSubarray(List<Integer> path, int idx){
        if(idx == nums.length){
            res.add(path);
            return;
        }

        List<Integer> temp = new ArrayList<>(path);
        temp.add(nums[idx]);

        generateSubarray(path, idx+1);
        generateSubarray(temp, idx+1);
    }

    public List<List<Integer>> subsets(int[] nums) {
        this.nums = nums;
        List<Integer> path = new ArrayList<>();
        generateSubarray(path, 0);
        return res;
    }
}