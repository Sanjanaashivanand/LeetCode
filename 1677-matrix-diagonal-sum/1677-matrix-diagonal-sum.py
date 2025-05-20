class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        res = 0

        for i in range(n):
            res += mat[i][i]
            res += mat[n-i-1][i]
        
        if n%2!=0:
            res -= mat[n//2][n//2]
        
        return res
