class Solution {
    private int[] nums;
    private List<List<Integer>> res;
    private int N;

    private void backtrack(ArrayList<Integer> path, HashMap<Integer, Integer> map){
        if(path.size() == N){
            res.add(new ArrayList<>(path));
            return;
        }

        for(int i: map.keySet()){
            if(map.get(i)==0) continue;
            
            int count = map.get(i);

            path.add(i);
            map.put(i, count-1);

            backtrack(path, map);

            path.remove(path.size()-1);
            map.put(i, count);
        }
    }

    public List<List<Integer>> permuteUnique(int[] nums) {
        this.nums = nums;
        this.N = nums.length;
        this.res = new ArrayList<>();

        HashMap<Integer, Integer> map = new HashMap<>();

        for(int i: nums){
            map.put(i, map.getOrDefault(i, 0)+1);
        }

        ArrayList<Integer> path = new ArrayList<>();
        backtrack(path, map);

        return res;

    }
}