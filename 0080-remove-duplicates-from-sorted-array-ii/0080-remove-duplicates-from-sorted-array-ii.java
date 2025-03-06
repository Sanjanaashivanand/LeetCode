class Solution {
    public int removeDuplicates(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int k = 0;

        for(int i: nums){
            map.put(i, map.getOrDefault(i, 0) + 1);
            if (map.get(i) <= 2) {
                nums[k] = i;
                k++;
            }
        }

        return k;   
    }
}