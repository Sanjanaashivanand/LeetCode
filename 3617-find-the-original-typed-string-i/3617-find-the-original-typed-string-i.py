class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        n, ans = len(word), 1
        for i in range(1, n):
            if word[i - 1] == word[i]:
                ans += 1
        return ans