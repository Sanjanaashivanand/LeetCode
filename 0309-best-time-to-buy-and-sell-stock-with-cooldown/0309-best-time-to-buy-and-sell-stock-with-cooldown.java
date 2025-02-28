class Solution {
    public int buyorsell(int idx, boolean buy, int[] prices, int[][] dp){
        if(idx >= prices.length){
            return 0;
        }
        
        if(dp[idx][buy ? 1:0] != -1) return dp[idx][buy ? 1:0];

        int profit = 0;
        if(buy){
            profit = Math.max(-prices[idx] + buyorsell(idx+1, false, prices, dp),
                                    buyorsell(idx+1, true, prices, dp));
        }
        else{
            profit = Math.max(prices[idx] + buyorsell(idx+2, true, prices, dp),
                                    buyorsell(idx+1, false, prices, dp));
        }

        return dp[idx][buy ? 1:0] = profit;
    }

    public int maxProfit(int[] prices) {
        int n = prices.length;
        int[][] dp= new int[n][2];

        for(int i=0; i<n; i++){
            for(int j=0; j<2; j++){
                dp[i][j] = -1;
            }
        }

        return buyorsell(0, true, prices, dp);
    }
}