class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = [0] * n

        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i-1], height[i])

        right = [0] * n
        right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])

        total = 0
        for i in range(0, n):
            if min(left[i], right[i]) - height[i] > 0:
                total += min(left[i], right[i]) - height[i]

        return total
        