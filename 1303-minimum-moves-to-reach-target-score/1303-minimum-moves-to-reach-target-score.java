class Solution {
    public int minMoves(int target, int maxDoubles) {
        int i=0;
        int moves = 0;
        while(target > 1){
            if(maxDoubles == i){
                moves += target-1;
                break;
            }

            if(target%2==0 && i<maxDoubles){
                target = target/2; 
                i++;
            }
            else{
                target--;
            }
            moves++;
        }

        return moves;
    }
}