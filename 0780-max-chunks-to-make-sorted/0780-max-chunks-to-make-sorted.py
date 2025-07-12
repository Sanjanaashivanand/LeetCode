class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        expected_sum = 0
        curr_sum = 0

        res = 0

        for i in range(0, len(arr)):
            expected_sum += i 
            curr_sum += arr[i]

            if expected_sum == curr_sum:
                res+=1

        return res
            