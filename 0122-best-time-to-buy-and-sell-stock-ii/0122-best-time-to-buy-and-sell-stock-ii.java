class Solution {
    public int buyorsell(int idx, boolean buy, int[] prices, int[][] dp){
        if(idx == prices.length){
            return 0;
        }
        
        if(dp[idx][buy ? 1:0] != -1) return dp[idx][buy ? 1:0];

        int profit = 0;
        if(buy){
            profit = Math.max(-prices[idx] + buyorsell(idx+1, false, prices, dp),
                                    buyorsell(idx+1, true, prices, dp));
        }
        else{
            profit = Math.max(prices[idx] + buyorsell(idx+1, true, prices, dp),
                                    buyorsell(idx+1, false, prices, dp));
        }

        return dp[idx][buy ? 1:0] = profit;
    }

    public int maxProfit(int[] prices) {
        int[][] dp = new int[prices.length+1][2];
        dp[prices.length][1] = 0;
        dp[prices.length][1] = 0;

        for(int i=prices.length-1; i>=0; i--){
            int profit;
            for(int buy =0; buy<=1; buy++){
                if(buy == 1){
                    profit = Math.max(-prices[i] + dp[i+1][0], dp[i+1][1]);
                }
                else{
                    profit = Math.max(prices[i] + dp[i+1][1],
                                    dp[i+1][0]);
                }
                dp[i][buy] = profit;
            }
        }

        return dp[0][1];

    }
}