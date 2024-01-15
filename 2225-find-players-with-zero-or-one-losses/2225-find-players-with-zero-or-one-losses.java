class Solution {
    public List<List<Integer>> findWinners(int[][] matches) {
        HashMap<Integer, int[]> map = new HashMap<>();
        
        for(int i=0; i<matches.length; i++){
            //winner
            int[] point = map.getOrDefault(matches[i][0], new int[2]);
            point[0]++;
            map.put(matches[i][0], point);
            
            //loser
            point = map.getOrDefault(matches[i][1], new int[2]);
            point[1]++;
            map.put(matches[i][1], point);
        }
        
        ArrayList<Integer> all_winners = new ArrayList<Integer>();
        ArrayList<Integer> lost_one = new ArrayList<Integer>();
        
        
        for(int i: map.keySet()){
            if(map.get(i)[1]==0){
                all_winners.add(i);
            }
            else if(map.get(i)[1]==1){
                lost_one.add(i);
            }
        }
        
        List<List<Integer>> res = new ArrayList<>();
        Collections.sort(all_winners);
        res.add(all_winners);
        Collections.sort(lost_one);
        res.add(lost_one);
        return res;
        
    }
}