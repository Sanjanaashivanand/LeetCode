class Solution {
    public long dpf(int curr, int[][] questions, long[] dp) {
        if (curr >= questions.length) {
            return 0;
        }
        
        if(dp[curr]!=-1) return dp[curr];

        long skip = dpf(curr + 1, questions, dp);
        long take = questions[curr][0] + (curr + questions[curr][1] + 1 < questions.length 
                                          ? dpf(curr + questions[curr][1] + 1, questions, dp) 
                                          : 0);
        
        return dp[curr] = Math.max(skip, take);
    }

    // public long mostPoints(int[][] questions) {
    //     int n = questions.length;
    //     long[] dp = new long[n];
    //     Arrays.fill(dp, -1);
    //     return dpf(0, questions, dp);
    // }

    public long mostPoints(int[][] questions) {
        int n = questions.length;
        long[] dp = new long[n+1];
        dp[n] = 0;

        for(int i=n-1; i>=0; i--){
            long skip = dp[i+1];
            long take = questions[i][0] + (i + questions[i][1] + 1 < questions.length 
                                          ? dp[i + questions[i][1] + 1]
                                          : 0);

            dp[i] = Math.max(skip, take);
        }

        return dp[0];
    }
}
