class Solution {
    private HashSet<List<Integer>> res = new HashSet<>();
    private int[] nums;
    private int target;

    private void generateSum(List<Integer> path, int sum, int idx){
        if(sum == target){
            res.add(path);
            sum = 0;
            return;
        }

        if(idx >= nums.length){
            return;
        }

        List<Integer> temp = new ArrayList<>(path);
        temp.add(nums[idx]);
        sum += nums[idx];

        if(sum>target){
            sum = 0;
            return;
        }

        generateSum(temp, sum, idx);
        generateSum(temp, sum, idx+1);

        sum -= nums[idx];
        generateSum(path, sum, idx+1);
    }

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<Integer> path = new ArrayList<>();
        Arrays.sort(candidates);
        this.target = target;
        this.nums = candidates;

        generateSum(path, 0, 0);
        return new ArrayList<>(res);
    }
}