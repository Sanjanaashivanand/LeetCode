class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isPalindrome(sub):
            return sub == sub[::-1]

        def expandAroundCenter(l, r):
            ans = 0
            while l>=0 and r<len(s):
                if s[l]!=s[r]:
                    return ans

                l-=1 
                r+=1
                ans+=1

            return ans
        
        res = 0
        for i in range(0, len(s)):
            res+=expandAroundCenter(i, i+1)
            res+=expandAroundCenter(i, i)

        return res