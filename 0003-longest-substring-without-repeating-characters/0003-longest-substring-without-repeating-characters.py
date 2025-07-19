class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0 
        j = 0
        window = set()
        n = len(s)
        res = 0

        while j < n:
            if s[j] not in window:
                window.add(s[j])
                res = max(j-i+1, res)
                j+=1

            else:
                while s[j] in window:
                    window.remove(s[i])
                    i+=1

        return res
