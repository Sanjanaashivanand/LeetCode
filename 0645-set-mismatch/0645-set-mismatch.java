class Solution {
    public int[] findErrorNums(int[] nums) {
        int[] res = new int[2];
        HashSet<Integer> set= new HashSet<Integer>();
        
        for(int i: nums){
            if(!set.add(i)){
                res[0] = i;
            }
        }
        
        for(int i: set){
            if(!set.contains(i-1) && i-1>0){
                res[1] = i-1;
                return res;
            }
            else if(!set.contains(i+1)){
                res[1] = i+1;
                return res;
            }
        }
        
        return res;
    }
}