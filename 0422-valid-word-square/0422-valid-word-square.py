class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        maxLen = -1
        for i in words:
            if len(i)>maxLen:
                maxLen = len(i)
        
        for i in range(len(words)):
            if len(words[i]) < maxLen:
                words[i] += "0" * (maxLen - len(words[i]))
        
        cols = []
        for j in range(0, maxLen):
            word = ""
            for i in range(len(words)):
                word += words[i][j]
            cols.append(word)
        
        for i in range(len(words)):
            if words[i]!=cols[i]:
                return False

        return True