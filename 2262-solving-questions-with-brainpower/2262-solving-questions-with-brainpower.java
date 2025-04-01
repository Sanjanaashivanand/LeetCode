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

    public long mostPoints(int[][] questions) {
        int n = questions.length;
        long[] dp = new long[n];
        Arrays.fill(dp, -1);
        return dpf(0, questions, dp);
    }
}
