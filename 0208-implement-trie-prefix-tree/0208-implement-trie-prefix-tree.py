class Trie(object):
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.endOfWord = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word):
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
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfWord
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)