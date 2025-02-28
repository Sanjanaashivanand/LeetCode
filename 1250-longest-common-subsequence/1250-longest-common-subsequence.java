class Solution {
    private int find(String text1, String text2, int id1, int id2, int[][] dp){
        if(id1<0 || id2<0) return 0;

        if(dp[id1][id2] != -1) return dp[id1][id2];

        if(text1.charAt(id1) == text2.charAt(id2)){
            return dp[id1][id2] = 1 + find(text1, text2, id1-1, id2-1, dp);
        }

        return dp[id1][id2] = Math.max(find(text1, text2, id1-1, id2, dp), 
                                        find(text1, text2, id1, id2-1, dp));
    }

    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length();
        int n = text2.length();

        int[][] dp = new int[m][n];
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                dp[i][j] = -1;
            }
        }

        return find(text1, text2, m-1, n-1, dp);
    }
}