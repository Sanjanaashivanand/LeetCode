class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        n = len(questions)
        self.res = -1


        def dfs(idx, dp):
            if idx >= n:
                return 0

            if dp[idx]!=-1:
                return dp[idx]

            #Pick
            pick = questions[idx][0] + dfs(idx+questions[idx][1]+1, dp)

            #Skip
            skip = dfs(idx+1, dp)

            dp[idx] = max(pick, skip)
            return dp[idx]

        dp = [-1]*(n+1)
        dfs(0, dp)
        return max(dp)