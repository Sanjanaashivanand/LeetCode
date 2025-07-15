class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        self.root = TrieNode()

        for word in wordDict:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.endOfWord = True

        def helper(start, memo):
            if start == n:
                return True

            if start in memo:
                return memo[start]

            curr = self.root

            for i, c in enumerate(s[start:]):
                if c not in curr.children:
                    break
                curr = curr.children[c]
                if curr.endOfWord:
                    if helper(start + i + 1, memo):
                        memo[start] = True
                        return True

            memo[start] = False
            return False
                
        memo = {}
        return helper(0, memo)


            