class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []  # Store top 3 suggestions at this node
        self.endOfWord = False

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        self.root = TrieNode()

        # Sort products to maintain lexicographical order
        products.sort()

        # Insert each product into Trie
        for word in products:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]

                # Store up to 3 lexicographically smallest words at each node
                if len(curr.words) < 3:
                    curr.words.append(word)

            curr.endOfWord = True

        # Now build results by walking the trie using the searchWord
        result = []
        curr = self.root

        for c in searchWord:
            if c in curr.children:
                curr = curr.children[c]
                result.append(curr.words)
            else:
                # If no such path, append empty lists for remaining chars
                result.extend([[]] * (len(searchWord) - len(result)))
                break

        return result
