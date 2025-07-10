class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])

        row = -1
        top = 0
        bottom = m - 1

        while top<=bottom:
            mid = (top+bottom)//2

            if matrix[mid][0] <= target <= matrix[mid][n-1]:
                row = mid
                break

            if matrix[mid][n-1] > target:
                bottom = mid - 1
            else:
                top = mid+1

        if row == -1:
            return False

        left = 0
        right = n-1

        while left<=right:
            mid = (left+right)//2

            if matrix[row][mid] == target:
                return True
                break

            if matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid+1

        return False