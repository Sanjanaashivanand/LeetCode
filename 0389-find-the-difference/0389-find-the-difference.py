class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = [0] * 26

        for c in s:
            count[ord(c)-ord('a')]+=1

        for c in t:
            count[ord(c)-ord('a')]-=1

        for i in range(0, 26):
            if count[i]!=0:
                return chr(i+ord('a'))
        
        return ""