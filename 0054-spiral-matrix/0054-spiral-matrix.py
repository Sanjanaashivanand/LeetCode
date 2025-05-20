class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        res = []

        m = len(matrix)        # number of rows
        n = len(matrix[0])     # number of columns

        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        while left <= right and top <= bottom:
            # Traverse from left to right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # Traverse downwards
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                # Traverse from right to left
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                # Traverse upwards
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res
