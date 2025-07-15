class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False for _ in range(n)]

        for i in range(len(s)):
            for word in wordDict:
                if i < len(word) - 1:
                    continue
                if i == len(word) - 1 or dp[i - len(word)] == True:
                    if s[i-len(word)+1:i+1] == word:
                        dp[i] = True 
                        break


        return dp[-1]
                