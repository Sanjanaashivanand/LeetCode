class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)

        def expand(string, start, end):
            i = start
            j = end

            while i>=0 and j<n:
                if s[i] == s[j]:
                    string = s[i] + string + s[j]
                else:
                    break
                i-=1
                j+=1
                
            return string

        res = ""
        for i in range(0, len(s)):
            center = expand(s[i], i-1, i+1)
            without = expand("", i, i+1)

            candidate = center if len(center) > len(without) else without
            if len(candidate) > len(res):
                res = candidate

        return res

        