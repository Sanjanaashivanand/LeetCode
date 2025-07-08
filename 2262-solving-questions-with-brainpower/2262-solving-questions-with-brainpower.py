class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        n = len(questions)
        dp = [0]*(n+1)

        for i in range(n-1, -1, -1):
            dp[i] = max(questions[i][0] + dp[min(i+questions[i][1]+1, n)], dp[i+1])

        return dp[0]