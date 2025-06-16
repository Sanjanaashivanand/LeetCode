class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1)!=len(word2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for i,j in zip(word1, word2):
            count1[ord(i) - ord('a')]+=1
            count2[ord(j) - ord('a')]+=1

        print(count1)
        print(count2)

        for i,j in zip(count1, count2):
            if i==j:
                continue
            
            if i == 0 or j == 0:
                return False

        
        count1.sort()
        count2.sort()

        for i,j in zip(count1, count2):
            if i!=j:
                return False

        return True