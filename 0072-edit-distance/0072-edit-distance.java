class Solution {
    public int dfs(int i, int j, String s, String t, int[][] dp){
        if(i == s.length() && j == t.length()) return 0;

        if(i == s.length()) return t.length() - j; 

        if(j == t.length()) return s.length() - i; 

        if(dp[i][j] != -1) return dp[i][j];

        int res = Integer.MAX_VALUE;
        if(s.charAt(i) == t.charAt(j)){
            res = dfs(i+1, j+1, s, t, dp);
        }
        else{
            res = 1 + Math.min(dfs(i+1, j+1, s, t, dp), 
                    Math.min(dfs(i, j+1, s, t, dp), dfs(i+1, j, s, t, dp)));
        }

        dp[i][j] = res;
        return res;
    }

    public int minDistance(String word1, String word2) {
        int[][] dp = new int[word1.length()+1][word2.length()+1];

        for(int i=0; i<=word1.length(); i++){
            for(int j=0; j<=word2.length(); j++){
                dp[i][j] = -1;
            }
        }

        return dfs(0, 0, word1, word2, dp);
    }
}

