class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isPalindrome(sub):
            return sub == sub[::-1]

        count = 0
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    count+=1

        return count
