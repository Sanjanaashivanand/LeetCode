class Solution(object):
    def longestObstacleCourseAtEachPosition(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: List[int]
        """
        stack = []
        result = []

        def upper_bound(arr, target):
            low, high = 0, len(arr)
            while low < high:
                mid = (low + high) // 2
                if arr[mid] <= target:
                    low = mid + 1
                else:
                    high = mid
            return low

        for height in obstacles:
            idx = upper_bound(stack, height)
            if idx == len(stack):
                stack.append(height)
            else:
                stack[idx] = height
            result.append(idx + 1)

        return result