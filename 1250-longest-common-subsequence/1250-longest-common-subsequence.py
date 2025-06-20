class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        def find(idx1, idx2, dp):
            if idx1<0 or idx2<0:
                return 0

            if dp[idx1][idx2]!=-1:
                return dp[idx1][idx2]

            if text1[idx1] == text2[idx2]:
                return 1 + find(idx1-1, idx2-1, dp)
            

            dp[idx1][idx2] = max(find(idx1, idx2-1, dp), find(idx1-1, idx2, dp))
            return dp[idx1][idx2]

        m = len(text1)
        n = len(text2)
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return find(len(text1)-1, len(text2)-1, dp)

        

            




        