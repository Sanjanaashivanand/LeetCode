class Solution {
    private List<List<Integer>> res = new ArrayList<>();
    private int[] nums;

    private void permute(List<Integer> path, int idx){
        if(idx == nums.length){
            res.add(path);
            return;
        }

        for(int j=idx; j<nums.length; j++){
            Collections.swap(path, idx, j);
            permute(new ArrayList<>(path), idx+1);
            Collections.swap(path, idx, j);
        }
    }

    public List<List<Integer>> permute(int[] nums) {
        this.nums = nums;
        List<Integer> path = new ArrayList<>();
        for(int i:nums){
            path.add(i);
        }
        permute(path,0);
        return res;
    }
}