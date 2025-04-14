class Solution {
    public int helper(int n, int[] dp){
        if(dp[n]!=-1) return dp[n];

        return dp[n] = helper(n-3, dp) + helper(n-2, dp) + helper(n-1, dp); 
    }

    public int tribonacci(int n) {
        if(n==0) return 0;
        if(n<=2) return 1;
        
        int[] dp = new int[n+1];
        Arrays.fill(dp, -1);
        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 1;

        helper(n, dp);
        return dp[n];
    }
}