class Solution {
    private List<List<Integer>> res = new ArrayList<>();
    private int[] nums;

    private void permutation(List<Integer> path, int idx){
        if(idx==nums.length){
            res.add(path);
            return;
        }

        for(int i=idx; i<nums.length; i++){
            Collections.swap(path, idx, i);
            permutation(new ArrayList<>(path), idx+1);
            Collections.swap(path, i, idx);
        }
    }

    public List<List<Integer>> permute(int[] nums) {
        this.nums = nums;

        List<Integer> path = new ArrayList<>();
        for(int i:nums){
            path.add(i);
        }
        permutation(path, 0);
        return res;
    }
}