class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word = ""
        i = 0
        j = 0

        while i<len(word1) and j<len(word2):
            word = word + word1[i]
            word = word + word2[j]
            i+=1
            j+=1
        
        while i<len(word1):
            word = word + word1[i]
            i+=1

        while j<len(word2):
            word = word + word2[j]
            j+=1

        return word