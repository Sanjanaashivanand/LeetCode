class WordDictionary(object):
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.endOfWord = False

    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = self.TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True
        
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        n = len(word)

        def dfs(idx, curr):
            if idx == n:
                return curr.endOfWord

            find = word[idx]

            if find == '.':
                for child in curr.children.values():
                    if dfs(idx + 1, child):
                        return True
                return False
            else:
                if find in curr.children:
                    return dfs(idx+1, curr.children[find])
                return False

        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)