class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        window = set() 
        i = 0
        j = 0
        
        while j < len(s):
            if s[j] not in window:
                window.add(s[j])
                j+=1
                res = max(res, len(window))
            else:
                window.remove(s[i])
                i+=1

        return res


        