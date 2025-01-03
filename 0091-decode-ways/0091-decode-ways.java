class Solution {
    public int numDecodings(String s) {
        if (s == null || s.length() == 0 || s.charAt(0) == '0') {
            return 0; // No valid decodings if the string is empty or starts with '0'
        }

        int[] dp = new int[s.length() + 1];
        dp[0] = 1; // Base case: 1 way to decode an empty string
        dp[1] = 1; // Base case: 1 way to decode if the first character is not '0'

        for (int i = 2; i <= s.length(); i++) {
            // Single-digit decoding
            if (s.charAt(i - 1) != '0') {
                dp[i] = dp[i - 1];
            }

            // Two-digit decoding
            int twoDigit = Integer.parseInt(s.substring(i - 2, i));
            if (twoDigit >= 10 && twoDigit <= 26) {
                dp[i] += dp[i - 2];
            }
        }

        return dp[s.length()];
    }
}