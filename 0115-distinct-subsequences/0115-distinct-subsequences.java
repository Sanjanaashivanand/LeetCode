class Solution {
    public int numDistinct(String s, String t) {
        int m = s.length();
        int n = t.length();
        
        int[][] dp = new int[m + 1][n + 1];
        
        // Base case: An empty string t can be formed from any prefix of s, so set dp[i][0] = 1 for all i
        for (int i = 0; i <= m; i++) {
            dp[i][0] = 1;  // One way to form an empty t from any prefix of s
        }
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s.charAt(i - 1) == t.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        
        return dp[m][n];
    }
}
