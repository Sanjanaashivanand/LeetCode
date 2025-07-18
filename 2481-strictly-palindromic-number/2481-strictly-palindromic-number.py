class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        for base in range(2, n-1):
            bases = []
            num = n

            while num!=0:
                bases.append(num%base)
                num = num//base 
    
            if bases!=bases[::-1]:
                return False

        return True