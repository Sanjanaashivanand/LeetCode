class Solution {
    public int[][] mergeArrays(int[][] nums1, int[][] nums2) {
        Map<Integer, Integer> map = new TreeMap<>();
        
        for(int[] i: nums1){
            map.put(i[0], i[1]);
        }

        for(int[] i: nums2){
            map.put(i[0], map.getOrDefault(i[0],0)+i[1]);
        }

        int[][] res = new int[map.size()][2];

        int k = 0;
        for(int i: map.keySet()){
            res[k][0] = i;
            res[k][1] = map.get(i);
            k++;
        }

        return res;
    }
}