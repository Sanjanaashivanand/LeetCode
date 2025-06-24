class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freq_s = {}
        freq_t = {}

        for i in s:
            if i not in freq_s:
                freq_s[i] = 0
            freq_s[i] += 1

        for i in t:
            if i not in freq_t:
                freq_t[i] = 0
            freq_t[i] += 1

        if len(freq_s)!=len(freq_t):
            return False

        for i in s:
            if i not in freq_t:
                return False
            if freq_s[i] != freq_t[i]:
                return False

        return True