class Solution(object):
    def largestRectangleArea(self, heights):
        heights.append(0)  # Sentinel to flush the stack
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                top = stack.pop()
                height = heights[top]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area

