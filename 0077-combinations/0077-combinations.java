class Solution {
    private List<List<Integer>> res = new ArrayList<>();

    private void combination(int idx, List<Integer> path, int n, int k){
        if(path.size()==k){
            res.add(path);
            return;
        }

        if(idx>n) return;

        List<Integer> copy = new ArrayList<>(path);
        copy.add(idx);
        combination(idx+1, copy, n, k);
        combination(idx+1, path, n, k);
        return;
    }

    public List<List<Integer>> combine(int n, int k) {
        combination(1, new ArrayList<>(), n, k);
        return res;
    }
}