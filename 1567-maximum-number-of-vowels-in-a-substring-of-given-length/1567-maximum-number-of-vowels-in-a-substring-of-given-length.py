class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = set(['a','e','i','o','u'])
        i = 0
        j = 0
        
        res = 0

        count = 0
        for j in range(0, k):
            if s[j] in vowels:
                count += 1

        for j in range(k, len(s)):
            res = max(res, count)
            if s[j] in vowels:
                count+=1

            if s[i] in vowels:
                count -= 1
            i+=1

        return max(res, count)
            
            


