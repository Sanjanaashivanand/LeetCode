class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        res = []

        def isPalindrome(word):
            return word == word[::-1]

        def findPartition(start, curr):
            if start == n:
                res.append(list(curr))
                return 

            for end in range(start+1, n+1):
                if isPalindrome(s[start:end]):
                    findPartition(end, curr + [s[start:end]])
        
        findPartition(0, [])
        return res