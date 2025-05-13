class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1, len(s)):
            sub = s[:i]
            if len(s)%len(sub)!=0: continue
            n = len(s)/len(sub)
            print(sub)
            if sub * n == s: return True
        
        return False