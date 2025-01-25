class Solution {
    public int[] lexicographicallySmallestArray(int[] nums, int limit) {
        int[] numsSorted = new int[nums.length];
        for (int i=0; i<nums.length; i++) numsSorted[i]=nums[i];
        Arrays.sort(numsSorted);

        HashMap<Integer, List<Integer>> map = new HashMap<>();
        int currGroup = 0;
        List<Integer> list = new ArrayList<>();
        list.add(numsSorted[0]);

        HashMap<Integer, Integer> groupMap = new HashMap<>();
        groupMap.put(numsSorted[0], currGroup);

        for(int i=1; i<nums.length; i++){
            if(Math.abs(numsSorted[i]-numsSorted[i-1])<=limit){
                list.add(numsSorted[i]);
            }
            else{
                map.put(currGroup, list);
                currGroup++;
                list = new ArrayList<>();
                list.add(numsSorted[i]);
            }
            groupMap.put(numsSorted[i], currGroup);
        }
        map.put(currGroup, list);
        
        for(int i=0; i<nums.length; i++){
            int num = nums[i];
            int group = groupMap.get(num);
            nums[i] = map.get(group).get(0);
            map.get(group).remove(0);
        }

        return nums;
    }
}