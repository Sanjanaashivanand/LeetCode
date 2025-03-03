class Solution {
    public boolean recurse(int i, int j, String s, String p, int[][] dp){
        if(j >= p.length()) {
            return i == s.length();  // If pattern is exhausted, s must also be exhausted
        }

        if(dp[i][j] != -1) {
            return dp[i][j] == 1;  // Return the memoized result
        }

        boolean match = i < s.length() && (s.charAt(i) == p.charAt(j) || p.charAt(j) == '.');

        if(j + 1 < p.length() && p.charAt(j + 1) == '*'){
            // Two possibilities for '*' to match:
            // 1. Skip the '*' and the preceding character in the pattern
            // 2. Match the character and recurse with one more character in s
            boolean result = recurse(i, j + 2, s, p, dp) || (match && recurse(i + 1, j, s, p, dp));
            dp[i][j] = result ? 1 : 0;  // Memoize the result
            return result;
        }

        if(match) {
            boolean result = recurse(i + 1, j + 1, s, p, dp);
            dp[i][j] = result ? 1 : 0;  // Memoize the result
            return result;
        }

        dp[i][j] = 0;  // Memoize failure
        return false;
    }

    public boolean isMatch(String s, String p) {
        int[][] dp = new int[s.length() + 1][p.length() + 1];
        for(int i = 0; i <= s.length(); i++) {
            for(int j = 0; j <= p.length(); j++) {
                dp[i][j] = -1;  // Initialize dp table with -1 (indicating uncalculated state)
            }
        }

        return recurse(0, 0, s, p, dp);
    }
}
