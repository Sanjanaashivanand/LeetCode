class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
       
        
        rev = s[::-1]
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == rev[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])


        return n - dp[0][0] 
        
        