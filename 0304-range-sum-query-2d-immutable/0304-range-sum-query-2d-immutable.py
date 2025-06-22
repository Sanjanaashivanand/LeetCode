class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])

        # prefix[i][j] = sum of submatrix from (0,0) to (i-1,j-1)
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                self.prefix[i+1][j+1] = (
                    matrix[i][j]
                    + self.prefix[i][j+1]
                    + self.prefix[i+1][j]
                    - self.prefix[i][j]
                )

    def sumRegion(self, r1, c1, r2, c2):
        """
        :type r1: int
        :type c1: int
        :type r2: int
        :type c2: int
        :rtype: int
        """
        return (
            self.prefix[r2+1][c2+1]
            - self.prefix[r1][c2+1]
            - self.prefix[r2+1][c1]
            + self.prefix[r1][c1]
        )
