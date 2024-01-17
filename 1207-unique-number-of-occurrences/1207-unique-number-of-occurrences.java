class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

        for(int i: arr){
            map.put(i, map.getOrDefault(i, 0)+1);
        }

        HashSet<Integer> set = new HashSet<Integer>();
        for(int i: map.keySet()){
            if(set.add(map.get(i))==false){
                return false;
            }
        }
        return true;
    }
}