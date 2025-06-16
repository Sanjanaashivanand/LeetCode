class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0: 
            return True

        i = 0
        j = 0

        for j in range(0, len(t)):
            if s[i] == t[j]:
                i+=1
                j+=1
            if i==len(s):
                return True
        
        return i==len(s)