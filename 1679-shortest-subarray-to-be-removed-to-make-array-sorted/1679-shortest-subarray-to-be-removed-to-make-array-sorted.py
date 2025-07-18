class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        n = len(arr)

        # Step 1: Find non-decreasing prefix
        left = 0
        while left + 1 < n and arr[left] <= arr[left + 1]:
            left += 1

        # Already sorted
        if left == n - 1:
            return 0

        # Step 2: Find non-decreasing suffix
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        # Initialize result as removing either all after prefix or all before suffix
        result = min(n - left - 1, right)

        # Step 3: Try to merge prefix and suffix
        i = 0
        j = right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                result = min(result, j - i - 1)
                i += 1
            else:
                j += 1

        return result
