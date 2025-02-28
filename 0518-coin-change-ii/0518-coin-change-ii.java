class Solution {
    public int find(int amount, int[] coins, int idx, int[][] dp) {
        if (amount < 0 || idx >= coins.length) {
            return 0;
        }

        if(dp[amount][idx]!=-1) return dp[amount][idx];

        if (amount == 0) {
            return 1;
        }

        int includeCurrentCoin = find(amount - coins[idx], coins, idx, dp);
        int excludeCurrentCoin = find(amount, coins, idx + 1, dp);

        return dp[amount][idx] = includeCurrentCoin + excludeCurrentCoin;
    }

    public int change(int amount, int[] coins) {
        int[][] dp = new int[amount+1][coins.length];
        for(int i=0; i<=amount; i++){
            for(int j=0; j<coins.length; j++){
                dp[i][j] = -1;
            }
        }
        return find(amount, coins, 0, dp);
    }
}
