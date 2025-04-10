class Solution {
    public int candy(int[] ratings) {
        int n = ratings.length;
        int[] dp = new int[n];

        for(int i=0; i<n; i++){
            dp[i] = 1;
        }

        for(int i=1; i<n; i++){
            if(ratings[i]>ratings[i-1]){
                dp[i] = dp[i-1]+1;
            }
        }

        int sum = dp[ratings.length - 1];
        for(int i=n-2; i>=0; i--){
            if(ratings[i]> ratings[i+1]){
                dp[i] = Math.max(dp[i], dp[i+1]+1);
            }
            sum += dp[i];
        }
        

        return sum;
    }
}

