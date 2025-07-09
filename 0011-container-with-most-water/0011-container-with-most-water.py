class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l = 0 
        r = n - 1
        res = 0

        while l<r:
            res = max(res, min(height[l], height[r]) * (r-l))

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return res

            
        