class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        copy = sorted(arr)

        expected_sum = 0
        curr_sum = 0

        res = 0

        for i in range(0, len(arr)):
            curr_sum += arr[i]
            expected_sum += copy[i]

            if curr_sum == expected_sum:
                res += 1

        return res