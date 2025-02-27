class Solution {
    public boolean isNStraightHand(int[] hand, int groupSize) {
        int n = hand.length;
        if(n%groupSize != 0) return false;
        
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i: hand) map.put(i, map.getOrDefault(i,0)+1);
        
        Arrays.sort(hand);
        
        for(int i=0;i<n;i++){
            int num = hand[i];
            
            if(map.get(num)>0){

                for(int j = num; j < num+groupSize; j++){
                    if(map.getOrDefault(j,0)==0) return false;
                    map.put(j, map.get(j)-1);
                }
            }
        }
    
        return true;
    }
}