class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10**9+7
        if n<3:
            return [1,1,2][n]

        f0,f1,f2 = 1,1,2
        for i in range(3,n+1):
            fn = (2*f2 + f0) % mod
            f0,f1,f2 = f1,f2,fn
        return f2
        

        