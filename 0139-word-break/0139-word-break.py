class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True

        for i in range(n-1, -1, -1):
            for word in wordDict:
                if i+len(word)<=n and s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)]

                if dp[i]:
                    break

        return dp[0]

