class Solution {
    private HashSet<List<Integer>> res = new HashSet<>();
    private int[] nums;
    private int target;

    private void compute(List<Integer> path, int curr, int idx){
        if(curr == target){
            res.add(path);
            return;
        }

        if(idx == nums.length || curr>target){
            return;
        }

        List<Integer> temp = new ArrayList<>(path);
        temp.add(nums[idx]);
        curr += nums[idx];

        compute(temp, curr, idx+1);

        curr -= nums[idx];
        while (idx + 1 < nums.length && nums[idx] == nums[idx + 1]) {
            idx++;
        }
        compute(path, curr, idx+1);

    }

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        this.nums = candidates;
        this.target = target;
        Arrays.sort(nums);
        List<Integer> path = new ArrayList<>();
        compute(path, 0, 0);
        return new ArrayList<>(res);
    }
}