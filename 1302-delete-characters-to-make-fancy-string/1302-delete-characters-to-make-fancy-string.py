class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""

        i = 0
        
        while i < len(s):
            res += s[i]
            if i<len(s)-1 and s[i] == s[i+1]:
                j = i+1
                while j<len(s) and s[j] == s[i]:
                    j+=1
                i = j
                res+=s[j-1]
            else:
                i+=1
        
        return res