class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int indexDiff, int valueDiff) {
        TreeSet<Long> set = new TreeSet<>();

        for(int i=0; i<nums.length; i++){
            long curr = (long)nums[i];

            Long floor = set.floor(curr);
            if(floor!=null && Math.abs(floor - curr) <= valueDiff) return true;

            Long ceil = set.ceiling(curr);
            if(ceil!=null && Math.abs(ceil - curr) <= valueDiff) return true;

            set.add(curr);

            if(i >= indexDiff){
                set.remove((long) nums[i-indexDiff]);
            }
        }

        return false;
    }
}