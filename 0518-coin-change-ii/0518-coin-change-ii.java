class Solution {
    public int change(int amount, int[] coins) {
        // Initialize the dp array with 0's, and set dp[0] = 1
        int[] dp = new int[amount + 1];
        dp[0] = 1;  // There's 1 way to make 0 amount (use no coins)
        
        // Iterate through all coins
        for (int coin : coins) {
            // Update the dp array for each amount that can be formed using the current coin
            for (int i = coin; i <= amount; i++) {
                dp[i] += dp[i - coin];  // Add the ways to make (i - coin) to the current dp[i]
            }
        }
        
        return dp[amount];  // Return the number of ways to make the amount
    }
}
