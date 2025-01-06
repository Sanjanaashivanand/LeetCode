class Solution {
    public int[] minOperations(String s) {
        int n = s.length();
        int[] res = new int[n];
        int balls = 0;
        int moves = 0;

        for(int i=0; i<n; i++){
            res[i]=balls+moves;
            moves = moves + balls;
            balls += s.charAt(i)-'0';
        }

        balls=0;
        moves=0;

        for(int i=n-1; i>=0; i--){
            res[i] += balls+moves;
            moves = moves + balls;
            balls += s.charAt(i)-'0';
        }

        return res;
    }
}