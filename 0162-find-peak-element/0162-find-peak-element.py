class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = max(nums)

        for i,val in enumerate(nums):
            if val == max_val:
                return i