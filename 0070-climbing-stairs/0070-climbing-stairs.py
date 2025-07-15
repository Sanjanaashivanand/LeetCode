class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        
        n1 = 1
        n2 = 2
        count = 0

        for i in range(3, n+1):
            count = n1 + n2 
            n1 = n2 
            n2 = count

        return count if n>2 else n2