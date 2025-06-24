class Trie:
        def __init__(self):
            self.children = {}
            self.endOfWord = False

class Solution(object):

    def dfs(self, s, node, curr_sentence, idx):
        if idx == len(s):
            self.res.append(curr_sentence.strip())
            return

        curr = node
        word = ""

        for i in range(idx, len(s)):
            char = s[i]

            if char not in curr.children:
                break  # No valid continuation
            curr = curr.children[char]
            word += char

            if curr.endOfWord:
                new_sentence = curr_sentence + " " + word
                self.dfs(s, node, new_sentence, i + 1)


    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.root = Trie()

        for word in wordDict:
            curr = self.root

            for c in word:
                if c not in curr.children:
                    curr.children[c] = Trie()
                curr = curr.children[c]

            curr.endOfWord = True

        self.res = []
        self.dfs(s, self.root, "", 0)
        return self.res


        
                

        