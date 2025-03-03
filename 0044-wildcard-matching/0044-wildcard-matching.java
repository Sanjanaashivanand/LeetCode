class Solution {
    // Memoization table to store the results of subproblems
    private int[][] dp;

    public boolean recurse(int i, int j, String s, String p){
        // If we have reached the end of both s and p, it's a match
        if(i >= s.length() && j >= p.length()) return true;
        
        // If we reached the end of p but s has remaining characters
        if(j >= p.length()) return false;

        // If this subproblem has already been solved, return the cached result
        if(dp[i][j] != -1) return dp[i][j] == 1;

        // Matching logic for character or wildcard '?'
        boolean match = i < s.length() && (s.charAt(i) == p.charAt(j) || p.charAt(j) == '?');

        // If the current character in pattern is '*', it can match zero or more characters from s
        if(p.charAt(j) == '*') {
            // Either skip '*' or consume one character from s
            boolean result = recurse(i, j + 1, s, p) || (i < s.length() && recurse(i + 1, j, s, p));
            dp[i][j] = result ? 1 : 0; // Store the result
            return result;
        }

        // If current characters match, move both pointers forward
        if(match) {
            boolean result = recurse(i + 1, j + 1, s, p);
            dp[i][j] = result ? 1 : 0;
            return result;
        }

        // If no match, store the result as false
        dp[i][j] = 0;
        return false;
    }

    public boolean isMatch(String s, String p) {
        // Initialize the dp table with -1 (indicating unvisited states)
        dp = new int[s.length() + 1][p.length() + 1];
        for(int i = 0; i <= s.length(); i++) {
            for(int j = 0; j <= p.length(); j++) {
                dp[i][j] = -1; // Initializing with -1 to indicate no value computed yet
            }
        }
        
        return recurse(0, 0, s, p);
    }
}
